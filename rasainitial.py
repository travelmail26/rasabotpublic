"""



cd /Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot_notsensitive_version

pip3 install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate

rasa data convert nlu -f yaml --data=./wellness-check-bot-master/data --out=data

rasa train
rasa shell

##for more data
f
rasa run actions --debug

#need to activate for custom actions in a different terminal
#cd /Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot
#source viren/bin/activate
# rasa run actions

##for creating aws instance

ec2 instance search ubuntu
configure instance details

add storage. details 8 gigs is

select existing group

under source drop down menu click anywhere
add rule, add http and under source anywhere
click launch

click on e2c. name instance

copy public ipv4 address on instance bar 54.90.47.150

#ubunut is the user name of my aws server


ssh -i /Users/gregoryferenstein/Downloads/rasabot1.pem ubuntu@3.220.111.85
#ssh command with is elastic ip
#note IP changes when instance changes
caused a too open permission error
chmod 400 /Users/gregoryferenstein/Downloads/rasabot1.pem

had to delete end ip address from file

git clone https://github.com/travelmail26/rasabot.git

#set up virtual env on aws
sudo apt-get install python3-venv


python3 -m venv --system-site-packages ./venv.\venv\Scripts\activate
#to activate
python3 -m venv ./venv
source ./venv/bin/activate
pip install -U pip

##to create a persistant IP create an elastic IP and assign it to the instance and create a name

##create port opening security. click on security for the instance at bottom on console


add inbound rule
port range 5000-6000
source type anywhere

attach policy to ec2 instance awsdenyall

#install python packages
pip freeze > requirements.txt #on local machine and upload to github
pip
pip3 install -r requirements.txt

##installing rasa x outside virtual environment

cd .. for root folder
sudo apt-get update

curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.38.1/install.sh

sudo bash ./install.sh

cd /etc/rasa
sudo docker-compose up -d

sudo python3 rasa_x_commands.py create --update admin me rasatest

ssh -keygen -t rsa -b 4096 -f git-deploy-key

-then in virtual environment
pip install --upgrade pip==20.2
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
to start: rasa x    
The server is running at http://localhost:5002/login?username=me&password=XAAfTDtj3BW0
@3.220.111.85
http://3.220.111.85:5002/login?username=me&password=XAAfTDtj3BW0

#if get error during procerss need to add memory
go to actions, templates and images in the instance aws console and turn size to 100

then under images ami's and launch when ready
select launch wizard1 or existing launchg instance
select existing pem file for secutiry
choose elastic IP for new instance

## starting instance
ssh -i /Users/gregoryferenstein/Downloads/rasabot1.pem ubuntu@3.220.111.85
cd rasabot
git pull
source ./venv/bin/activate

#separate windwow for actions
cd rasabot
git pull
source ./venv/bin/activate
rasa run actions

#starting ngrok on instance
ngrok http 5005


##ran into a error and modified telegram api with this code https://github.com/botfront/botfront/issues/517

##
in post man make a post request http://localhost:5005/webhooks/rest/webhook

change to json
{
    "sender" : "sender102",
    "message" : "jobs linkedin"
}


##instructions on deployment for docker

ran into error with incompatible with port_bindings and need to downgrade

copy requirements.txt and paste in actions file
then put in a line in the docker compose file
depends_on:
      - requirements

ran into issues with docker, had to downgrade rasa and then ran into gspread package so added a new file

remove rasa from requirements.txt in file in the actions folder. erased all packages that were not native. only included asana gspread and a few others
command: docker-compose build

docker-compose up --remove-orphans
#actions folder got error for dialog asana so changed from actions.dialogasanalink
get rid of txt file extension
chmod +x apache_install

Setting up aws
sudo ./apache_install
sudo apt-get install apache2
sudo apache2ctl configtest

##setting up continous deployment

Create a github secret 
DOCKER_BOT_SECRET
paste aws key in the value

Create a new token
https://github.com/settings/tokens/new
git pull https://${{ secrets.DOCKER_BOT_ACCESS_TOKEN}}@github.com/S1LV3RJ1NX/dockerized-bot.git

note: name it dockertoken or something, click on repo and token options
token 

telegram
http://3.220.111.85/docker_bot/webhooks/telegram/webhook

##setting up ssl certificate

installed nginx on free domain pointing to elastic ip on aws
http://rasabot.tk/
sudo unlink /etc/nginx/sites-enabled/default #removed default accessible sites by nginx

sudo nano /etc/nginx/sites-available/reverse-proxy.conf
172 is a local generated ip for docker software

server {

    server_name rasabot.tk; # your servername here

    access_log /var/log/nginx/reverse-access.log;
    error_log /var/log/nginx/reverse-error.log;

    #reverse proxy to rasa container
    location / {
        proxy_pass  http://172.17.0.1:5005;
    }
}

server {
    listen       80;
    server_name  rasabot.tk; # your servername here

    access_log /var/log/nginx/reverse-access.log;
    error_log /var/log/nginx/reverse-error.log;

    #reverse proxy to rasa container
    location /docker_bot {
        proxy_pass  http://172.17.0.1:5005;
    }
}



change configuation
webhook_url: "https://rasabot.tk/webhooks/telegram/webhook"
test with sudo nginx -t
sudo systemctl restart nginx

sudo certbot --nginx
select 1 for no redirect

checked firewall turned off sudo ufw status and this was a problem
sudo ufw enable
sudo ufw allow 'Nginx Full'


####notes on github action

The file github workflow  in the hidden .github/workflows/main.yml

it is copied below and responds once git push is executed from the master git branch

# This is a basic workflow to help you get started with Actions
name: CI

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ master ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  deploy_to_instance:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:     
      - name: executing remote ssh commands using ssh key
        uses: appleboy/ssh-action@master
        with:
          host: 3.220.111.85 # IP of instance
          username: ubuntu 
          key: ${{ secrets.DOCKER_BOT_SECRET}} # This is secret of pem file
          port: 22
          script: |
            cd rasabot
            git status
            # This is the url for repo since it's private repo we need token else we can directly pull
            git pull https://${{ secrets.DOCKER_BOT_ACCESS_TOKEN}}@github.com/travelmail26/rasabot.git
            #sudo docker-compose down
            #source ./venv/bin/activate
            #sudo rm models/*.gz
            #rasa train
            #sudo docker-compose build
            #sudo docker-compose up

### using ngrok

command: ngrok http 5005

copy and paste forwarding https address in configuation



##migrating to  rasa 3.0

rasa data migrate -d /Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot/domain2toreplace.yml --out /Users/gregoryferenstein/Dropbox/visualstudiostest/selfbot/domain.yml

google contacts

required installed files from quickstart guide
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

#git access token

created an environemtal variable
touch .env
then defined a asana token ASANA_ACCESS_TOKEN=<token>
created a config.py in actions
from dotenv import load_dotenv
import os

load_dotenv()

asana_access_token = os.environ.get('ASANA_ACCESS_TOKEN')



Launching on google cloud

gcloud compute ssh --zone "northamerica-northeast2-a" "selfbot"  --project "boreal-furnace-352219"


got an error installing and had to modify install.sh with nano and replace the curl with this

curl -O https://bootstrap.pypa.io/pip/3.6/get-pip.py

had to modify docker compose file manually
"""




