import json
import requests
from requests.auth import HTTPBasicAuth

devIP = "192.168.99.128"
usr = "cisco"
pwd = "cisco"
headers = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}
url = f"https://{devIP}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=4"

request = requests.get(url, auth=HTTPBasicAuth(usr, pwd), headers=headers, verify=False)

if request.status_code == 200:
    data = request.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {request.status_code}")
    print(request.text)