import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

device_list = ['192.168.99.129', '192.168.99.130', '192.168.10.1']
user = "cisco"
pwd = "cisco"

#Iterate through device list and grab OSPF information
for device in device_list:
    