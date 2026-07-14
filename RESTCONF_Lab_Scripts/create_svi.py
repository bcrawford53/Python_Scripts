import requests
from requests.auth import HTTPBasicAuth
from devices import SWITCH_SM_LAB
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Create Switch Dictionary Object and Pull variables needed for RESTCONF connection
switch_dict = SWITCH_SM_LAB
user = switch_dict['username']
pwd = switch_dict['password']
hostname = switch_dict['host']

