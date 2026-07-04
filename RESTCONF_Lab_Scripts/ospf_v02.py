import json
import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES

#Enable OSPF
for device,list in DEVICES.items():
    print(f"Configuring OSFP for {device}")
    device_list = list
    
    #Create OSPF process
    ospf_url = f"https://{device_list['ip']}/restconf/data/Cisco-IOS-XE-native:native/router"
    payload = {"Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {"process-id": [{"id":10,"network": [{"ip":"192.168.100.0","wildcard":"0.0.0.255","area":0}]}]}
        }
    }}
    headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
    response = requests.request("PATCH", url=ospf_url, auth=HTTPBasicAuth(device_list['usr'],device_list['passwd']),
                                headers=headers, json=payload, verify=False )
    if response.status_code == 200:
        print("OSPF Enabled")
    else:
        print("Mistake somewhere")
    ospf_response = requests.request("GET", url=ospf_url, auth=HTTPBasicAuth(device_list['usr'],device_list['passwd']),
                                headers=headers, verify=False )
    print(ospf_response.text)