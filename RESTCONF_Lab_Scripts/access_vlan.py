import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from devices import SWITCH_SM_LAB

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Set the variables: Username, Password, BaseURL, IP, Hostname
switch_dict = SWITCH_SM_LAB
user = switch_dict['username']
pwd = switch_dict['password']
base_url = f"https://{switch_dict['ip']}/restconf/data"
IP = switch_dict['ip']
host_name = switch_dict['host']
deviceA_port_dict = switch_dict['host_interfaces'][0]
deviceB_port_dict = switch_dict['host_interfaces'][1]
deviceA_intf = switch_dict['host_interfaces'][0]['HOST_A']['interface']
deviceB_intf = switch_dict['host_interfaces'][1]['HOST_B']['interface']
deviceA_vlan = switch_dict['host_interfaces'][0]['HOST_A']['vlan']
deviceB_vlan = switch_dict['host_interfaces'][1]['HOST_B']['vlan']
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}

#Configure Access VLANs for DeviceA on Switch
vlan_access_url = base_url + f"/openconfig-interfaces:interfaces/interface={deviceA_intf.replace('/','%2F')}/openconfig-if-ethernet:ethernet/switched-vlan"
devA_payload = {"openconfig-vlan:switched-vlan": {
    "config": {
        "interface-mode": "ACCESS",
        "access-vlan": deviceA_vlan
    }
}}

try:
    devA_response = requests.request("PATCH", url=vlan_access_url, auth=HTTPBasicAuth(user,pwd), headers=headers, data=json.dumps(devA_payload), 
                                      verify=False)
    if devA_response.status_code == 204:
        print(f"Success! Status Code: {devA_response.status_code}\nVLAN {deviceA_vlan} configured on Interface {deviceA_intf}\n")
    else:
        print("Failed")
except Exception as e:
    print(f"Failed due to: {e}")
 

 #Configure Access VLANs for DeviceB on Switch
vlan_access_url = base_url + f"/openconfig-interfaces:interfaces/interface={deviceB_intf.replace('/','%2F')}/openconfig-if-ethernet:ethernet/switched-vlan"
devA_payload = {"openconfig-vlan:switched-vlan": {
    "config": {
        "interface-mode": "ACCESS",
        "access-vlan": deviceB_vlan
    }
}}

try:
    devB_response = requests.request("PATCH", url=vlan_access_url, auth=HTTPBasicAuth(user,pwd), headers=headers, data=json.dumps(devA_payload), 
                                      verify=False)
    if devA_response.status_code == 204:
        print(f"Success! Status Code: {devB_response.status_code}\nVLAN {deviceB_vlan} configured on Interface {deviceB_intf}")
    else:
        print("Failed")
except Exception as e:
    print(f"Failed due to: {e}")

