import requests
from requests.auth import HTTPBasicAuth
import json
from devices import DEVICES

#Headers for HTTP Request
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}

#GET Config of Interfaces Before Change
try:
    for device in DEVICES.values():
        intf_url = f"https://{device["ip"]}/restconf/data/Cisco-IOS-XE-native:native/interface"
        response = requests.request("GET", auth=HTTPBasicAuth(device["usr"],device["passwd"]), url=intf_url, headers=headers, verify=False)
        if response.status_code == 200:
            print("*"*20,f"Results from: {device["ip"]}","*"*20)
            print(response.text)
            print("\n")
            print("*"*30)
        else:
            print('Sorry error somewhere')

except Exception as e:
    print(f"Failed to execute: {e}")

#Enable the interfaces
try:
    for device in DEVICES.values():
        print("*"*10, f"Enabling the Interfaces on {device["ip"]}","*"*10)
        IP=device["ip"]
        for intf in device.keys():
            intf_url = f"https://{IP}/restconf/data/Cisco-IOS-XE-native:native/interface/{intf[:-1]}={intf[-1]}/shutdown"
            response = requests.request("DELETE", url=intf_url, auth=HTTPBasicAuth(device["usr"],device['passwd']),
                                        headers=headers, verify=False )
            if response.status_code>=200:
                print(f"Interface {intf} Enabled!")
            else:
                print("Error Interface Not Enabled")

except Exception as e:
    print(f"Sorry error made: {e}")


    >>> for value in DEVICES.values():
...    for intf in value['interfaces'].values():
...       print(intf)
... 
{'ip': '192.168.100.1', 'mask': '255.255.255.252'}
{'ip': '192.168.100.5', 'mask': '255.255.255.252'}
{'ip': '192.168.100.9', 'mask': '255.255.255.252'}
{'ip': '192.168.100.2', 'mask': '255.255.255.252'}
{'ip': '192.168.100.13', 'mask': '255.255.255.252'}
{'ip': '192.168.100.17', 'mask': '255.255.255.252'}
>>> 
>>> 
>>> for value in DEVICES.values():
...    for intf,ips in value['interfaces'].items():
...      print(f"interface={intf}  IP info={ips}"
... 
... 
... 
... 
... )
... 
interface=GigabitEthernet4  IP info={'ip': '192.168.100.1', 'mask': '255.255.255.252'}
interface=GigabitEthernet3  IP info={'ip': '192.168.100.5', 'mask': '255.255.255.252'}
interface=GigabitEthernet2  IP info={'ip': '192.168.100.9', 'mask': '255.255.255.252'}
interface=GigabitEthernet4  IP info={'ip': '192.168.100.2', 'mask': '255.255.255.252'}
interface=GigabitEthernet3  IP info={'ip': '192.168.100.13', 'mask': '255.255.255.252'}
interface=GigabitEthernet2  IP info={'ip': '192.168.100.17', 'mask': '255.255.255.252'}
>>> 

