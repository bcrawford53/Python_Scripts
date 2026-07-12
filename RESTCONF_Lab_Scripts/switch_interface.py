import requests
from requests.auth import HTTPBasicAuth
import json
from devices import SWITCH_SM_LAB
import sys

#Place SWITCHES dictionary into object for later use
switch_dict = SWITCH_SM_LAB

#Base URL for RESTCONF access to device
base_url = f"https://{switch_dict['ip']}/restconf/data"

#Enable Routing Interface to WAN-B
intf_2_wanb = switch_dict['route_interface']['interface']
ipaddr_2_wanb = switch_dict['route_interface']['ip']
ip_mask_2_wanb = switch_dict['route_interface']['mask']
user = switch_dict['username']
pwd = switch_dict['password']
intf = intf_2_wanb.replace("/", "%2F")  # Encode slashes for URL

intf_ip_url = base_url + f"/openconfig-interfaces:interfaces/interface={intf}"
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
ip_payload = {"openconfig-interfaces:interfaces": [
    {
        "name": "GigabitEthernet1/0/2",
        "config": {
            "name": "GigabitEthernet1/0/2",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True
        }
    }
]}
try:
    ip_response = requests.request("GET", intf_ip_url, auth=HTTPBasicAuth(user, pwd), headers=headers, verify=False)
    if ip_response.status_code == 200:
        ip_response_data = ip_response.json()
        if ip_response_data['openconfig-interfaces:interface'][0]['config']['enabled'] == True:
            print(f"The Interface {ip_response_data['openconfig-interfaces:interface'][0]['name']} is already enabled.")
            print(ip_response.status_code)
        else:
            ip_response = requests.request("PATCH", intf_ip_url, auth=HTTPBasicAuth(user, pwd), headers=headers, data=json.dumps(ip_payload), verify=False)
            if ip_response.status_code == 204:   
                print(f"Interface {intf_2_wanb} enabled successfully.")
            else:
                print(f"Failed to enable interface {intf_2_wanb}. Status code: {ip_response.status_code}, Response: {ip_response.text}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while enabling interface {intf_2_wanb}: {e}")

#Make Interface a routed port
#route_url = intf_ip_url + "/openconfig-if-ethernet:ethernet/config/cisco-xe-openconfig-if-ethernet-ext:switchport'"
route_url = intf_ip_url + "/openconfig-if-ethernet:ethernet/config"
print('\n\n\n')
print(route_url)
#route_payload = {"cisco-xe-openconfig-if-ethernet-ext:switchport": False}
route_payload =  {"openconfig-if-ethernet:config":{"cisco-xe-openconfig-if-ethernet-ext:switchport": False
  }
}

try:
    port_response = requests.request("PATCH", url=route_url, auth=HTTPBasicAuth(user, pwd), headers=headers, data=json.dumps(route_payload), 
                                     verify=False)
    if port_response.status_code == 204:
        print(f"Turned switchport off on device {switch_dict['host']}, on port {intf_2_wanb}")
    else:
        print(f"Failed to turn off switchport on device {switch_dict['host']}, on port {intf_2_wanb}")
        exit()
except Exception as e:
    print(f"Failed to turn off swithport because of {e}")

print('\n\n\n')
#Add IP address to the interface
ip_url = intf_ip_url + "/subinterfaces/subinterface=0/openconfig-if-ip:ipv4"
payload = {"openconfig-if-ip:ipv4":
           {"addresses":{
               "address": [
                   {
                       "ip": ipaddr_2_wanb,
                       "config": {
                           "ip": ipaddr_2_wanb,
                           "prefix-length": ip_mask_2_wanb
                       }
                   }
               ]
           }}
}
try:
    response = requests.request("PATCH", ip_url, auth=HTTPBasicAuth(user, pwd), headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 204:
        print(f"IP address {ipaddr_2_wanb}/{ip_mask_2_wanb} configured successfully on interface {intf_2_wanb}.")
    else:
        print(f"Failed to configure IP address {ipaddr_2_wanb}/{ip_mask_2_wanb} on interface {intf_2_wanb}. Status code: {response.status_code}, Response: {response.text}")    
except Exception as e:
    print(f"Failed to configure IP address")




