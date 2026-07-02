import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES
import json

base_url = f"https://{DEVICES['rtr1']['ip']}/restconf/data/Cisco-IOS-XE-native:native/"
headers = {"Accept":"application/yang-data+json", "Content-Type": "application/yang-data+json"}
USER = DEVICES["rtr1"]["usr"]
PWD = DEVICES["rtr1"]["passwd"]
try:
    enable_interface_url = base_url + "/interface/GigabitEthernet=4/shutdown"
    response = requests.request("DELETE", auth=HTTPBasicAuth(USER,PWD), url=enable_interface_url, headers=headers, verify=False)
    print(response.text)

    #Assign IP address to the interface
    ip_addr_url = base_url + "/interface/GigabitEthernet=4"
    payload = {
            "Cisco-IOS-XE-native:GigabitEthernet": {
                "name": "4",
                "description": "Link to RTR2",
                "ip": {
                "address": {
                    "primary": {
                    "address": "192.168.100.1",
                    "mask": "255.255.255.252"
                    }
                },
                },
            }}
            
    ip_response = requests.request("PATCH", auth=HTTPBasicAuth(USER,PWD), url=ip_addr_url, headers=headers, data=json.dumps(payload), verify=False)
    print(ip_response.text)
except Exception as e:
    print(f"Failed to connect: {e}")