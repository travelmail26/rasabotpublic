from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
from actions.dialogasanalink import list_tasks_all, get_task_details, list_tasks_numbered_names, update_task_date, get_task_by_id, create_subtask_and_assignee, search_asana_people_by_name, create_crm_contact_from_google_contacts


import csv

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']



from google.oauth2 import service_account


#SERVICE_ACCOUNT_FILE = '/Users/gregoryferenstein/Downloads/peopleapipublic-ae92f115a147.json'

# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot/token_zazzle.json'):
        creds = Credentials.from_authorized_user_file('/Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot/token_zazzle.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             '/Users/gregoryferenstein/Downloads/client_secret_483158769689-aq57bp9akmqr4cs9vpj5t3nsb7agl6an.apps.googleusercontent.com.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token_zazzle.json', 'w') as token:
    #         token.write(creds.to_json())

    try:
        service = build('people', 'v1', credentials=creds)

        #print ('this is the service', service)

        #profile = service.people().get(resourceName='people/c63810788897573286', personFields='names').execute()

        #print ('this is the profile directory', dir(profile))
        #print ('this is the profile', profile)
        #print ('json dump', json.dumps(profile.to_json))

        #search = service.people().searchContacts(query='firt', readMask='names').execute()

        #searchresults = search.get('results', [])

        # for result in searchresults:
        #     print ('result', result)
        #     names = result.get('person').get('names')
        #     print ('**$$names', names[0]['displayName'])

        #print ('search', search)

        # Call the People API
        #print('List 10 connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=100,
            personFields='names,emailAddresses,biographies,externalIds').execute()
        connections = results.get('connections', [])

        lis = [['ID', 'Name', 'Note']]
        for person in connections:
            #print ("***", person, "***")
            names = person.get('names', [])
            notes = person.get('biographies', [])
            id = person.get('resourceName', [])
            email = person.get('emailAddresses', [])
            print ('email: ', email)

            create_crm_contact_from_google_contacts(id, names[0].get('displayName'), notes[0].get('value'), email=email[0].get('value'))

            print ('names', names[0].get('displayName'))
            #print ('this is the name', names, 'this is the note', notes)
            #if names:
                #name = names[0].get('displayName')
            #print ('print', names[0].get('displayName'))

            #print('this display name', name)
            #if notes:
            #note = notes[0].get('value')
            #print(notes[0].get('value'))
            #print ('the id', id)





            ###dictionary attempt####
        # service = build('people', 'v1', credentials=creds)
        # results = service.people().connections().list(
        #     resourceName='people/me',
        #     pageSize=10,
        #     personFields='names,emailAddresses,biographies,externalIds').execute()
        # connections = results.get('connections', [])

        # lis = [['ID', 'Name', 'Note']]
        # for person in connections:
        #     #print ("***", person, "***")
        #     people_dic['ID'].append(person.get('resourceName'))
        #     people_dic['Name'].append(person.get('names')[0].get('displayName'))
        #     people_dic['Note'].append(person.get('biographies')[0].get('value'))



        ##new code

        # row_list = [["ID", "Name", "Note"],
        #      [1, "Linus Torvalds", "Linux Kernel"],
        #      [2, "Tim Berners-Lee", "World Wide Web"],
        #      [3, "Guido van Rossum", "Python Programming"]]

        # lis = ['ID', 'Name', 'Note']
        # for person in connections:
        #     lis.append([names[0].get('displayName'), notes[0].get('value'))
        # with open('contactslist.csv', 'w', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(lis)


    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()