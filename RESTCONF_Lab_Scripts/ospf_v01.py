import json
import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES


#Enable OSPF on the routers
try:
    for device in DEVICES.values():
        print("*"*10, f"Enabling OSPF on {device['ip']}","*"*10)
        IP=device["ip"]
        ospf_url = f"https://{IP}/restconf/data/Cisco-IOS-XE-native:native/router"
        payload = {
            "Cisco-IOS-XE-native:router": {
                "Cisco-IOS-XE-ospf:router-ospf": {
                    "ospf": {
                        "process-id": [
                            {
                                "id": 10
                            }
                        ]
                    }
                }
            }
        }
        response = requests.request("PATCH", url=ospf_url, auth=HTTPBasicAuth(device["usr"],device['passwd']),
                                    headers={"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"},
                                    json=payload, verify=False )
        if response.status_code>=200:
            print(f"OSPF Enabled on {device['ip']}!")
        else:
            print("Error OSPF Not Enabled")
except Exception as e:
    print(f"Sorry error made: {e}")









{
  "Cisco-IOS-XE-native:router": {
    "Cisco-IOS-XE-ospf:router-ospf": {
      "ospf": {
        "process-id": [
          {
            "id": 10
          }
        ]
      }
    }
  }
}
