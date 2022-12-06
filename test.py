from __future__ import print_function
import os.path

import pandas as pd
import asana
import json
import re
from Levenshtein import distance
from datetime import datetime
import ast
import requests



##google
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials


# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

###dialog aasana



# 



#    writer.write(str(list_tasks_all('placeholder')))

#f = open('guru99.txt', 'r')



# pip3 install python-Levenshtein


###google contacts test

####google people api





from actions.dialogasanalink import list_tasks_all, get_task_details, list_tasks_numbered_names, update_task_date, get_task_by_id, create_subtask_and_assignee, search_asana_people_by_name, create_crm_contact_from_google_contacts, list_tasks_numbered_names_with_notes, extract_email_from_crm, update_task_note
#from actions.config import asana_access_token
from actions.gmail_create_draft_api import gmail_create_draft, update_google_sheet

#list_tasks_numbered_names('test')



# pip3 install python-Levenshtein

# replace with your personal access token. 

#personal_access_token = '1/1133333906014563:888dc8d408e0d9939ea127b442330f44'
#personal_access_token = asana_access_token

#client = asana.Client.access_token('1/1202356680885092:afe23e9506d695c8d8301c1119ed5b47')


#list_tasks_numbered_names_with_notes('firstname2')

# result = extract_email_from_crm('1202441038958954')
# print ('result', result)

# client = asana.Client.access_token('1/1202356680885092:afe23e9506d695c8d8301c1119ed5b47') #phil brown asana token

# string = 'test task 2 : gid: 1202356681134809'

# capture = re.search(r"gid:\s(\d+)", string).group(1)
                    
# print ("***capture", capture) 

# update_task_note('1202356681134809', 'from test.py')

#{'gid': '1202371139788623', 'name': 'biz crm', 'resource_type': 'project'} for phil brown asana

#gf workplace gid 14437628389122
#for workspace in philbrown
# result = client.workspaces.get_workspace('1202356765339323', {'param': 'value', 'param': 'value'}, opt_pretty=True)

# projectsinphilbrown = client.projects.get_projects_for_workspace('1202356765339323', {'param': 'value', 'param': 'value'}, opt_pretty=True)

# result = client.tasks.get_tasks_for_project('1202356681134796', {'param': 'value', 'param': 'value'}, opt_pretty=True, opt_fields="name, gid, notes")



# for i in projectsinphilbrown:
        
#         for task in client.tasks.find_by_project(i['gid'], {"opt_expand":"name, notes, tags"
#                                                                         }):
#             print('DEBUG: ', task['name'], '\n\n')
#             if distance('test task', task['name']) <= 50 or distance('test task', task['notes']) <= 50:
#                 print('task name after distance command', task['name'])
# for i in result:
#     print (i)
# import operator
# import time
# import itertools
# print('this is the list', itertools.islice(result, 1))

#print ('***the project result', result[0])


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# creds = None
# if os.path.exists('token.json'):
#     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# #If there are no (valid) credentials available, let the user log in.
# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             '/Users/gregoryferenstein/Downloads/client_secret_483158769689-1funkv8qf8l3ocqfhvceslk59d9qnl6v.apps.googleusercontent.com.json', SCOPES)
#         creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open('token.json', 'w') as token:
#         token.write(creds.to_json())

# try:
#     # Call the Gmail API
#     service = build('sheets', 'v4', credentials=creds)
#     # Call the Gmail API
#     spreadsheet_id = '1-RSIDhAxco6cHTGmeC3nDyZeGXH34Xvk95D__lKfa7U'  # TODO: Update placeholder value.



#     service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, valueInputOption='RAW' , range='Sheet1', body={'values': [['6', 'f']]}).execute()
# except HttpError as error:
#     print(f'An error occurred: {error}')



#gmail_create_draft(sendto=result, messagebody='from test.py')

update_google_sheet()
#gmail_create_draft()

#result = client.workspaces.get_workspaces({'param': 'value', 'param': 'value'}, opt_pretty=True)




#workspaces {'gid': '1202356680885092', 'email': 'philbrown4455@gmail.com', 'name': 'Phil Brown', 'photo': None, 'resource_type': 'user', 'workspaces': [{'gid': '1202356765339323', 'name': 'My Workspace', 'resource_type': 'workspace'}]}

#result = client.workspaces.get_workspace('1202356765339323', {'param': 'value', 'param': 'value'}, opt_pretty=True)


#result = client.tasks.search_tasks_for_workspace('1202356765339323', {'text': 'zazzle', 'param': 'value'}, opt_pretty=True)


# print ('this enumeraged list from api', list_tasks_numbered_names('task'))


# listed_tasks_from_slot = '1. get a job interview id: 1175500331946249; \n2. Learn to use Nunchucks id: 1175289994987646;'
# my_regex = '4.'

# capture = re.search(my_regex, listed_tasks_from_slot)
# print ('the capture', capture)
# print ('the capture', capture.group(0))

# def create_subtask_and_assignee(task_gid, name_new_task, name_given):
    

#     #select_assignee = "1. 'gid': '1201333765747686' divya; \n 2. 'gid': '1201368136618602' obed; \n 3. 'gid': '1201587130885312' siara; 4. 'gid': '1201587130885312' greg"

#     name_and_gid_dic = { '1201333765747686': 'divya', '1201368136618602': 'obed', '1201587130885312': 'siara', '14437627317215': 'greg'}

#     for i in name_and_gid_dic.items():
#         if name_given == i[1]:
#             name_to_gid = i[0]



#     result = client.tasks.create_subtask_for_task(task_gid, {'name': name_new_task, "assignee": name_to_gid, 'workspace' : '14437628389122', 'notes': 'note_description'}, opt_pretty=True)

#     print ('this is the task created', result)
#     return result


# replace with your personal access token. 


#personal_access_token = '1/1133333906014563:303966998052573c185e63f6ac4e7d99'

# Construct an Asana client
# client = asana.Client.access_token(personal_access_token)
# Set things up to send the name of this script to us to show that you succeeded! This is optional.
# client.options['client_name'] = "hello_world_python"
#client = asana.Client.access_token(personal_access_token)
# me = client.users.me()
# client.options['page_size'] = 100

# print('workspaces', me)


# # workspace = me['workspaces'][1]
# # workspace_gid = workspace['gid']

# print ('this is the workspace', workspace)

# test_gid = '1200763800865779'
# #test qq task id: 1200763800865779; otehr task 1175717687801625
# #i = client.users.get_users({'workspace': workspace}, opt_pretty=True)
# #create_subtask_and_assignee(test_gid, 'new task name', 'greg')

# search_asana_people_by_name('austin')

# def search_asana_people_by_name(person_name):
    

#     result = client.tasks.search_tasks_for_workspace(workspace_gid, {'?projects.all': '1200763800865901', 'text': person_name}, opt_pretty=True)


#     for i in result:
#         lst = []
#         new_open_string = "task gid: {}; name: {}" 

#         lst.append (new_open_string.format(i['gid'], i['name']))
#         #print (lst)
#         return lst



# search_asana_people_by_name('Tom')


#result = client.users.get_users_for_workspace(workspace['gid'], {'param': 'value', 'param': 'value'}, opt_pretty=True)

# for item in result:
#     print (item)

#x = client.projects.get_projects_for_workspace(workspace_gid, {'param': 'value', 'param': 'value'}, opt_pretty=True)

#for i in x:
#    print (i)

"""


###search google api serp

import requests

params = {
  'access_key': 'abe63facc89ff9448cfdbd44b0cd736e',
  'query': 'nyc "vivos" apnea',
  'num': 3
}

api_result = requests.get('http://api.serpstack.com/search', params)

api_response = api_result.json()

#print ("Total results: ", api_response['search_information']['total_results'])
#print ("Total results: ", api_response)

url_list = []

for number, result in enumerate(api_response['organic_results'], start=1):
    print ("%s. %s" % (number, result['title']))
    print ("%s. %s" % (number, result['url']))
    url_list.append(result['url'])


import requests
from bs4 import BeautifulSoup

URL = 'https://www.verywellhealth.com/alternative-treatments-for-sleep-apnea-3015327'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

for url in url_list:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    for element in soup.find_all("p"):
        print (element.get_text())




#with open('guru99.txt', 'w+') as writer:



#f.close() maybe after writing initial line



###serp api request









print ('file run above function')

def create_and_delegate_task(task_gid, name_new_task):
    
    name = name_new_task
    
    result = client.tasks.create_subtask_for_task(task_gid, {'name': name, "assignee": "1133333906014563", 'workspace' : '14437628389122'}, opt_pretty=True)

    return result

create_and_delegate_task('1176928685018316', 'delegatedtask jj2')


print('this is the task', client.tasks.find_by_id(task=1176928685018316))


def list_tasks_all():
    #https://stackoverflow.com/questions/36106712/how-can-i-limit-iterations-of-a-loop-in-python
    tasks_list = []
    for workspace in me['workspaces']:
        projects = client.projects.find_by_workspace(workspace['gid'], iterator_type=None)
        for project in projects:
            for index, task in zip(range(1), client.tasks.find_by_project(project['gid'], {"opt_expand":"name, projects"
                                                                        
                                                                                            })):

            #for task in client.tasks.find_by_project(project['gid'], {"opt_expand":"name, projects, workspace, \
            #                                                            gid, due_on, created_at, modified_at, completed, \
            #                                                            completed_at, assignee, parent, notes, tags"
            #                                                        }):
    
                #if distance(name, task['name']) <= 18:
                
                print(task)
                tasks_list.append(task)
                #   tasks_list.append(task['name'])

    return tasks_list
with open('fulltasklist.txt', 'w') as writer:
    writer.write(str(list_tasks_all()))




[{'gid': '1175717687801625', 'name': 'search jobs on linkedin', 'resource_type': 'task'}, {'gid': '1155260496865434', 'name': 'budget categories transactions', 'resource_type': 'task'}]"""

#https://stackoverflow.com/questions/56876193/trouble-using-dicts-parsed-by-ast



#for line in f.read():
#        line = ast.literal_eval(line)
#print(type(ast.literal_eval(as_string)))


#type(list_tasks_all('placeholder')))

#print(list_tasks_numbered_names('jobs linkedin'))


"""

with open('fulltasklist.txt', 'w') as writer:
    writer.write(str(list_tasks_all()))

i=[]
with open('fulltasklist.txt', 'r') as f:
    for i in f.readlines():
        if not i.strip():  # do nothing for empty lines
            continue
        i = ast.literal_eval(i)
        #print (i)
print ('this is it', type(i))

print ('this is listed i', i[0]['name'])


for item in i:
    if distance('linkedin', item['name']) <= 15:
        print (item['name'])
    
########



result = client.typeahead.typeahead_for_workspace('14437628389122', {"resource_type": "task", 'name': 'nunch', 'completed': 'True'}, opt_pretty=True)

for item in result:
    print ('this is a an itme ****', item)


#print(me['email'])

def list_tasks_all(name):
    #https://stackoverflow.com/questions/36106712/how-can-i-limit-iterations-of-a-loop-in-python
    tasks_list = []
    for workspace in me['workspaces']:
        projects = client.projects.find_by_workspace(workspace['gid'], iterator_type=None)
        for project in projects:
            #for index, task in zip(range(1), client.tasks.find_by_project(project['gid'], {"opt_expand":"name, projects, workspace, \

            for task in client.tasks.find_by_project(project['gid'], {"opt_expand":"name, projects, workspace, \
                                                                        gid, due_on, created_at, modified_at, completed, \
                                                                        completed_at, assignee, parent, notes, tags"
                                                                    }):
    
                #if distance(name, task['name']) <= 18:
                tasks_list.append(task)
                #   tasks_list.append(task['name'])

    return tasks_list
with open('fulltasklist.txt', 'w') as writer:
    writer.write(str(list_tasks_all('placeholder')))



def list_tasks_numbered_names(name):
    
    tasks_list = []
    tasks_list_numbered = []
    name_as_string = "'" + name + "'"
    print ('this is the name from function', name)

    #tasks_collected = client.tasks.search_tasks_for_workspace('14437628389122', {"opt_expand":"name, \
    #                                                            gid,  \
    #                                                            tags",
    #                                                            "completed": False
    #                                                            #"name": name
    #                                                        })
            
            
            
    for workspace in me['workspaces']:
        projects = client.projects.find_by_workspace(workspace['gid'], iterator_type=None)
        for project in projects:
            for task in client.tasks.find_by_project(project['gid'], {"opt_expand":"name, projects, workspace, \
                                                                    gid, due_on, created_at, modified_at, completed, \
                                                                    completed_at, assignee, parent, notes, tags",
                                                                    "completed": True
                                                                }):
        #print ('this is the task names', task['name'])
                
    print ('this is tasks collected', tasks_collected)
    
    for tasks in tasks_collected:
        print ('this is task inside the function', tasks)
                #if distance(name, task['name']) <= 50:
                #    tasks_list.append(task['name'] + ' id: ' + task['gid'] + ';')

now = datetime.now()
 
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#print(get_task_by_id('1137984743423265'))



#client.tasks.update_task('1174833394015231', {'name': 'task 1 in project one education added text'}, opt_pretty=True)

#x = client.tasks.get_task('1174833394015231', opt_pretty=True)


update_task_date('1174833394015231', 'april 15')



client.tasks.update_task('1174833394015231', {'notes': 'console added '}, opt_pretty=True)


#print ('DEBUG STATUS task', x['notes'])
#personal_access_token = '1/1133333906014563:888dc8d408e0d9939ea127b442330f44'

#def my_function(**kwargs):
#    print str(kwargs)

my_function(a=12, b="abc")

def my_function2(arg1, arg2, **kwargs):
	print (kwargs, arg1)
	print type((kwargs, arg1))
	print type((arg1, arg2))

	return kwargs


my_function2("one", "two", c='123')
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
#file_name = 'client_key.json'
#creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/gregoryferenstein/Downloads/agentnametest-vjyyhn-d455798841e6.json',scope)
#client = gspread.authorize(creds)
#sheet = client.open('dialogflow output').sheet1

#print (client)


blist = ['task1', 'task 2']

#print ('this is the numbered list', enumerate(blist))

l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
#print ('this is the object'. obj1)
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,2)))

for number, name in obj1:
    print ('this is the printed', number, name)


# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

sheet.append_row(
            ["from test doc", dt_string], 
            value_input_option='RAW', 
            insert_data_option=None, 
            table_range=None)


def foo():
     d = dict();
     d['str'] = "Tutorialspoint"
     d['x']   = 50
     return d
print (foo())


#############google contacts

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts']

def main():
    Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
# Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    print('List 10 connection names')
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='names,emailAddresses').execute()
    connections = results.get('connections', [])

    for person in connections:
        names = person.get('names', [])
        if names:
            name = names[0].get('displayName')
            print(name)


    #body = newContact = { "names": [{ "givenName": "John", "familyName": "Doe" }] }

    #service.people().updateContact(resourceName = 'people/c1589313158061148817', body=None, personFields='biographies', sources=None, updatePersonFields='test city', x__xgafv=None)

    
    print('List of all name with email id and phone number:\n')
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1500,
        personFields='names,nicknames,emailAddresses,phoneNumbers,biographies').execute()



    print ('TOP LINE', results)
    connections = results.get('connections', [])


    print (type(connections))

    for person in connections:
        names = person.get('names', [])
        notes = person.get('biographies')
        identifications = person.get('resourceName')
        nick = person.get('nicknames') 
        #print ('person', person)
        print (identifications)
    
    
    






    
    aContact = service.people().get(
    resourceName = 'people/c1589313158061148817',
    personFields = 'biographies' ).execute()
    notesNames = aContact['biographies'][0]        
    notesNames['value'] = 'changed bio qwe'

    aContact['biographies'] = notesNames

    result = service.people().updateContact(
    resourceName = 'people/c1589313158061148817',
    body = aContact, 
    updatePersonFields = 'biographies'
    ).execute()
    
    print ('search below')
    searchresult = service.people().searchContacts(pageSize=10, query='miami', 
    readMask='names,biographies', 
    sources=None, x__xgafv=None).execute()


    connections = searchresult.get('results', [])


#     """
#     i=0
#     for key in connections:

#         #print ('this is key names: ', key['person']['names'][0]['displayName'])
#         name = key['person']['names'][0]['displayName']
#         identification = key['person']['resourceName']
#         print (key)
#         print(f"\n{i}. name: {name}, id: {identification}")
#         i+=1

#     #update edit
    
#     aContact = service.people().get(
#     resourceName = 'people/c36943406266964946',
#     personFields = 'names,nicknames'
#     ).execute()
#     print ('this is acontact', aContact)
#     NickNames = aContact['nicknames'][0]        
#     NickNames['value'] = 'newNickName2'

#     aContact['nicknames'] = NickNames
#     result = service.people().updateContact(
#     resourceName = 'people/c36943406266964946',
#     body = aContact, 
#     updatePersonFields = 'nicknames'
#     ).execute()
    
    
#     i=1
#     for person in connections:
#         names = person.get('names', [])
#         emails = person.get('emailAddresses', [])
#         phones = person.get('phoneNumbers')
#         notes = person.get('biographies')
#         identifications = person.get('resourceName')
#         nick = person.get('nicknames') 
#         #print ('person', person)
#         print (identifications)

#         if names and emails:
#             name = names[0].get('displayName')
#             email = emails[0]['value']
#             identification = identifications[0]
#             try:
#                 phone = phones[0]['value']
#             except:
#                 pass
#             try:
#                 notes = notes[0]['value']
#             except:
#                 pass
#             print(f"\n{i}. {name} - {email} {phone} {notes} {identification} {nick}")
#             i+=1
#             """
# if __name__ == '__main__':
#     main()




"""






#print (workspace)



"""
