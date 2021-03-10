#this project is done with raspberry pi 3

#packages needed for this script
#sudo apt-get install python-setuptools
#sudo pip install twython

#Necessary packages
import random
import os
import sys
from twython import Twython

#variables for API 
CONSUMER_KEY =
CONSUMER_SECRET =
ACCESS_KEY =
ACCESS_SECRET = 

#API setup
api = Twython(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


api.update_status(status=sys.argv[1])
