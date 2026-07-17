import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from devices import SWITCH_SM_LAB

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

switch_dict = SWITCH_SM_LAB
hostname = switch_dict['host']
user = switch_dict['username']
pwd = switch_dict['password']
vlan_list = switch_dict['vlans']
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
url = "https://192.168.10.1/restconf/data/Cisco-IOS-XE-native:native/vlan/"
payload = {"Cisco-IOS-XE-native:vlan": {
    "Cisco-IOS-XE-vlan:vlan-list": [
        {"id":vlan_list[0]["id"],
         "name":vlan_list[0]["name"]},
         {"id":vlan_list[1]["id"],
         "name":vlan_list[1]["name"]},
         {"id":vlan_list[2]["id"],
         "name":vlan_list[2]["name"]}
    ]
}
}

try:
    response = requests.request("PUT", url=url, auth=HTTPBasicAuth(user,pwd), headers=headers,
                                json=payload, verify=False )
    if response.status_code >= 200:
        print(f"Success. ----Status Code: {response.status_code} ------")
        print(json.dumps(response.json(), indent=2))
    else:
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))
except requests.exceptions.JSONDecodeError:
    print(response.text or "The router returned an empty response.")