import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES

#Enable the interface and create a Subinterface for VLAN 90
try:
    pass
    for device, list in DEVICES.items():
        dev_list = list
        host = dev_list['ip']
        intf_num = dev_list['interfaces']['GigabitEthernet2']['name']
        USR = dev_list['usr']
        PASS = dev_list['passwd']
        intf_url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={intf_num}/shutdown"
        #Enable the interface
        headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
        response = requests.request("DELETE", url=intf_url, auth=HTTPBasicAuth(USR,PASS),
                                    headers=headers, verify=False)
        print(response.status_code)

        #Create a Subinterface for VLAN 90
        sub_url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/interface"
        IP = dev_list['interfaces']['GigabitEthernet2']['ip']
        MASK = dev_list['interfaces']['GigabitEthernet2']['mask']
        payload = {"Cisco-IOS-XE-native:interface": {
                        "GigabitEthernet": [
                            {
                                "name": "2.90",
                                "description": "RESTCONF VLAN 90 Subinterface",
                                "encapsulation": {
                                    "dot1Q": {
                                        "vlan-id": 90
                                    }
                                },
                                "ip": {
                                    "address": {
                                        "primary": {
                                            "address": IP,
                                            "mask": MASK
                                        }
                                    }
                                }
                            }
                        ]
                    }
        }       

        sub_response = requests.request("PATCH",url=sub_url,auth=HTTPBasicAuth(USR,PASS),
                                    headers=headers, json=payload, verify=False)
        print()
        print(sub_response.status_code)

except Exception as e:
    print("Error {e}")
