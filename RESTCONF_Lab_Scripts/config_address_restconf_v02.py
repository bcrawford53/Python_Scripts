import requests
from requests.auth import HTTPBasicAuth
import json
from devices import DEVICES

USR = "cisco"
PWD = "cisco"
HEADERS = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}
#Enable Interfaces
try:
    for device, value in DEVICES.items():
        print("+"*10, f"Enabling Interfaces on {device}","+"*10)
        device_dict = value
        hostip = device_dict['ip']
        for intf,ip in device_dict['interfaces'].items():
            print(f"Enabling interface: {intf}")
            intf_url = f"https://{hostip}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={ip['name']}/shutdown"
            response = requests.request("DELETE",url=intf_url, auth=HTTPBasicAuth(device_dict['usr'],device_dict['passwd']),
                                        headers=HEADERS, verify=False)
            if response.status_code >= 200 and response.status_code < 300:
                print("Interface enabled:")
                print(response.text)
            else:
                print("Interface not enabled")
            #Configure IP Address on Interface
            print(f"Adding IP address: {ip['ip']} to {intf}")
            payload = {"Cisco-IOS-XE-native:GigabitEthernet": 
                       {"name": f"{ip['name']}", "ip": 
                            {"address": {"primary": {"address": f"{ip['ip']}", "mask": f"{ip['mask']}"}}}
                            }
            }
            ipadd_intf_url = f"https://{hostip}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={ip['name']}/"
            ipadd_response = requests.request("PATCH", url=ipadd_intf_url, auth=HTTPBasicAuth(device_dict['usr'],device_dict['passwd']),
                                        json=payload, headers=HEADERS, verify=False)
            if ipadd_response.status_code >= 200 and ipadd_response.status_code < 300:
                print(f"\nIP address {ip['ip']} added to {intf}.")
except Exception as e:
    print(f"Error: {e}")