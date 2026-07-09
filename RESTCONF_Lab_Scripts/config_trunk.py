import requests
from requests.auth import HTTPBasicAuth
import json

host = "192.168.99.113"
usr = "netadmin"
pwd = "cisco123"

base_url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/interface"
headers = {"Accept":"application/yang-data+json","Content-Type":"application/yang-data+json"}

payload =  {"Cisco-IOS-XE-native:interface": 
            {"GigabitEthernet": [{
                "name": "1/0/1",
                "switchport-config": {
                "switchport": {
                    "Cisco-IOS-XE-switch:mode": {
                    "trunk": {
                    }
                    },
                    "Cisco-IOS-XE-switch:trunk": {
                    "native": {
                        "vlan": {
                        "vlan-id": 99
                        }
              }
            }
          }
            }
          }]
        }}

try:
    response = requests.request("PATCH", url=base_url, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=payload, verify=False)
    if response.status_code == 204:
        print(f"Success: {response.status_code}")
        print(response.status_code)
        print(response.text)
    else:
        print(f"Error somewhere {response.status_code}")
        print(response.status_code)
        print(response.text)
except Exception as e:
    print(e)
    print(response.status_code)
    print(response.text)
