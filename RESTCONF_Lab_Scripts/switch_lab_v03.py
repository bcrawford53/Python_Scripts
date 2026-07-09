import requests
from requests.auth import HTTPBasicAuth
import json
from devices import SWITCHES

usr = "netadmin"
pwd = "cisco123"


print(f"Adding VLANs to device: 192.168.99.155")
vlan_url = "https://192.168.99.155/restconf/data/native/vlan"
payload = {"Cisco-IOS-XE-native:vlan": {
    "Cisco-IOS-XE-vlan:vlan-list": [
        {"id": 10,"name":"DATA"},
        {"id":20,"name":"VoIP"},
        {"id":30,"name":"SECURITY"},
        {"id":99,"name":"NATIVE_VLAN"}
    ]
}}
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
try:
    response = requests.request("PUT",url=vlan_url, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=payload, verify=False)
    print(response.status_code)
except Exception as e:
    print("Failed, status code: ",response.status_code)
    print(f"Error:  {e}")
