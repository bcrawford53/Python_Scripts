import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("device_list.json","r") as file:
    json_file = file.read()
    json_dict = json.loads(json_file)
    print(type(json_dict))

for device in json_dict['Devices']:
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

    ip_payload = {"openconfig-if-ip:ipv4": {
                        "addresses": {
                            "address": [
                                {
                                    "ip": ipaddr,
                                    "config": {
                                        "ip": ipaddr,
                                        "prefix-length": sub_mask
                                    }
                                }
                                ]
                        }
                    }
                }
    ipurl = url + "/interface=GigabitEthernet2/subinterfaces/subinterface=0/openconfig-if-ip:ipv4"
    try:
        response_ip = requests.request("PATCH", url=ipurl, auth=HTTPBasicAuth(usr,pwd), headers=headers, json=ip_payload, verify=False)
        if response_ip.ok:
            print(f"Successfully configured {ipaddr}/{sub_mask}")
            print(json.dumps(response.json(), indent=2))
        else:
            print("Configuration failed.")
            print(json.dumps(response.json(), indent=2))
    except requests.exceptions.JSONDecodeError:
        print(response.text or "The router returned an empty response.")
