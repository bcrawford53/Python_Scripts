import requests
from requests.auth import HTTPBasicAuth
import json
from devices import SWITCHES

device_IPs = [SWITCHES["SWITCH_A"]['ip'], SWITCHES["SWITCH_B"]['ip']]
usr = "netadmin"
pwd = "cisco123"

for device in device_IPs:
    print(f"Adding VLANs to device: {device}")
    vlan_url = f"https://{device}/restconf/data/native/vlan"
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
        response = requests.request("PATCH",url=vlan_url, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=payload, verify=False)
        print(response.status_code)
    except Exception as e:
        print("Failed, status code: ",response.status_code)
        print(f"Error:  {e}")
