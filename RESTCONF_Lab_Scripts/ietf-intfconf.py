import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from devices import DEVICES

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#interate to each device and configure LAN interface
for device, device_dict in DEVICES.items():
    hostname = device
    ipaddr = device_dict['ip']
    user = device_dict['usr']
    pwd = device_dict['passwd']
    intf_list = list(device_dict['interfaces'])
    intf = intf_list[0]
    intf_ip = device_dict['interfaces']['GigabitEthernet2']['ip']
    intf_subnet = device_dict['interfaces']['GigabitEthernet2']['mask']
    headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
    base_url = f"https://{ipaddr}/restconf/data/ietf-interfaces:interfaces"

    #Enable Interface
    intf_url = base_url + f"/interface={intf_list[0]}"
    enable_intf_payload = {"ietf-interfaces:interface": 
            {"name": intf,
             "description":"LAN Interface",
             "type": "iana-if-type:ethernetCsmacd",
             "enabled": True,
             "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": intf_ip,
                    "netmask": intf_subnet
                    }
                ]
                }
            }}
             
    
    try:
        response = requests.request("PUT",url=intf_url, headers=headers, auth=HTTPBasicAuth(user,pwd),
                                json=enable_intf_payload, verify=False)
        if response.status_code >= 200:
            print(f"Enabled interface {intf_list[0]} on {hostname}")
            print(f"Success. ----Status Code: {response.status_code} ------")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Failed to enable interface {intf_list[0]} on {hostname}")
            print(response.status_code)
            print(json.dumps(response.json(), indent=2))
    except requests.exceptions.JSONDecodeError:
        print(response.text or "The router returned an empty response.")
