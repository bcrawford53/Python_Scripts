import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES

#Enable the interface and create a Subinterface for VLAN 90
try:
    pass
    for device, list in DEVICES.items():
        dev_list = list
        intf_url = f"https://{dev_list['ip']}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={list['interfaces']['GigabitEthernet2']['name']}/shutdown"
        #Enable the interface
        headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
        response = requests.request("DELETE", url=intf_url, auth=HTTPBasicAuth(dev_list['usr'],dev_list['passwd']),
                                    headers=headers, verify=False)

        #Create a Subinterface for VLAN 90
        subintf_url = f"https://{dev_list['ip']}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={list['interfaces']['GigabitEthernet2']['name']}"
        IP = dev_list['interface']['GigabitEthernet2']['ip']
        MASK = dev_list['interface']['GigabitEthernet2']['mask']
        payload = {"Cisco-IOS-XE-native:GigabitEthernet": {"name":"2.90", "description":"LAN Subinterface",
                                                           "encapsulation": {"vlan-id":90},
                                                           "ip":{"address": {
                                                               {"primary":
                                                                    {"address":IP,
                                                                     "mask":MASK}
                                                               }
                                                           }}}}
        sub_response = requests.request("PATCH",url=subintf_url,auth=HTTPBasicAuth(dev_list['usr'],dev_list['passwd']),
                                    headers=headers, json=payload, verify=False)
        if response == 200:
            print("Created subinterface")
        else:
            print("Something broke")
                                                        

except Exception as e:
    print("Error {e}")
