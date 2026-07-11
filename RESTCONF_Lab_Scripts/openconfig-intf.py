import requests
from requests.auth import HTTPBasicAuth
import json

with open("device_list.json","r") as file:
    json_file = file.read()
    json_dict = json.loads(json_file)
    print(type(json_dict))

for device in json_dict['Devices']:
    if device['ip'] == '192.168.10.1':
        pass
    else:
        #Enable the LAN interface
        usr = device['username']
        pwd = device['password']
        baseurl = f"https://{device['ip']}/restconf/data"
        url = baseurl + "/openconfig-interfaces:interfaces"
        headers = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}
        ipaddr = device['interfaces'][0]['ip_address']
        sub_mask = device['interfaces'][0]['mask']
        payload = {"openconfig-interfaces:interfaces": {
                    "interface": [
                        {
                            "name": "GigabitEthernet2",
                            "config": {
                            "name": "GigabitEthernet2",
                            "type": "iana-if-type:ethernetCsmacd",
                            "enabled": True
                            }
                        },
                    ]}}
        try:
            response = requests.request("PATCH", url=url, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=payload, verify=False)
            if response.status_code == 204:
                print(f"Interfaces enabled: ---Status Code--- {response.status_code}")
            else:
                print("Failed")
        except Exception as e:
            print(f"Failed session: {e}")

        ip_payload = {
                         "openconfig-if-ip:ipv4": {
                            "addresses": {
                                "address": [
                                    {
                                    "ip": ipaddr,
                                    "config": {
                                        "ip": ipaddr,
                                        "prefix-length": sub_mask
                                    },
                                    "state": {
                                        "ip": ipaddr,
                                        "prefix-length": sub_mask
                                    }
                                    }]
                            }}
                        }
        try:
            ip_url = baseurl + "/openconfig-if-ip:ipv4/interface=GigabitEthernet2"
            response_ip = requests.request("PATCH", url=ip_url, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=ip_payload, verify=False)
            if response_ip.status_code == 204:
                print(f"IP address configured: ---Status Code--- {response_ip.status_code}")
            else:
                print("Failed")
        except Exception as e:
            print(f"Failed session: {e}")   
        
        