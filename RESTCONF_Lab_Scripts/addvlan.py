from requests.auth import HTTPBasicAuth
import requests
from devices import SWITCHES
import json

try:
    user = "netadmin"
    passwd = "cisco123"
    for device, vl_list in SWITCHES.items():
        print(f"Configuring VLANS for {device}")
        vlan_list = vl_list
        vlan_url = f"https://{vlan_list['ip']}/restconf/data/Cisco-IOS-XE-native:native/vlan"
        payload = {"Cisco-IOS-XE-native:vlan": {
                            "Cisco-IOS-XE-vlan:vlan-list": [
                                {"id":10,
                                "name":"DATA"},
                                {"id":20,
                                    "name":"VoIP"},
                                    {"id":30,
                                    "name":"CAMERA"}
                   ]}}
        headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
        response = requests.request("PUT", url=vlan_url, auth=HTTPBasicAuth(user,passwd), json=payload, headers=headers,
                                    verify=False)
        print(response.status_code)

        if response.json():
            print(response.json())


except Exception as e:
    print(f"Script failed: {e}")

