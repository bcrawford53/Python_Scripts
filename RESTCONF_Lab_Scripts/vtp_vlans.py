import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from devices import SWITCH_SM_LAB
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Place SWITCHES dictionary into object for later use
switch_dict = SWITCH_SM_LAB

#Base URL for RESTCONF access to device
base_url = f"https://{switch_dict['ip']}/restconf/data"
print(base_url)
print('\n\n')

#Grab username and password from the dictionary and create headers for RESTCONF requests
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
user = switch_dict['username']
pwd = switch_dict['password']

#Configure VTP Mode Transparent
vtp_url = base_url + "/Cisco-IOS-XE-native:native/vtp"
vtp_payload = {"Cisco-IOS-XE-native:vtp": {"Cisco-IOS-XE-vtp:mode": {"transparent": [None]}}}
print(vtp_url)
print('\n\n')
 
try:
    vtp_response = requests.request("PATCH", vtp_url, auth=HTTPBasicAuth(user, pwd), headers=headers, data=json.dumps(vtp_payload), verify=False)
    if vtp_response.status_code == 204:
        print(f"VTP mode set to transparent successfully on device: {switch_dict['host']}.")
    else:
        print(f"Failed to set VTP mode to transparent on device: {switch_dict['host']}. Status code: {vtp_response.status_code}, Response: {vtp_response.text}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while setting VTP mode to transparent on device: {switch_dict['host']}: {e}")

#Configure VLANs on the switch
vlan1 = switch_dict['vlans'][0]
vlan2 = switch_dict['vlans'][1]
vlan3 = switch_dict['vlans'][2]
vlan_list = [vlan1,vlan2,vlan3]

vlan_payload = {"openconfig-vlan:vlans":{ 
    "vlan" : [
        {"vlan-id" : vlan1['id'],
            "config":
             {"vlan-id":vlan1['id'], "name":vlan1['name']}
            },
        {"vlan-id": vlan2['id'],
            "config":
             {"vlan-id":vlan2['id'], "name":vlan2['name']}
            },
        {"vlan-id": vlan3['id'],
            "config":
             {"vlan-id":vlan3['id'], "name":vlan3['name']}
            }
        ]
    }
    }

vlan_url = base_url + "/openconfig-vlan:vlans"

print("\n\nConfiguring VLANS on the switch...")
try:
    vlan_response = requests.request("PATCH", url=vlan_url, auth=HTTPBasicAuth(user,pwd), data=json.dumps(vlan_payload),
                                     headers=headers, verify=False)
    if vlan_response.status_code == 204:
        print(f"Success. Added Vlans to device: {switch_dict['host']}")
        for vlan in vlan_list:
            print(f"Vlans Added: {vlan['id']} name: {vlan['name']}")
    else:
        print(f"Failed to add vlans to device: {switch_dict['host']}. Status code: {vlan_response.status_code}, Response: {vlan_response.text}")

except Exception as e:
    print(f"Failed to add vlans to device: {switch_dict['host']}")
    print(f"Error: {e}")