import requests
from requests.auth import HTTPBasicAuth
from devices import SWITCH_SM_LAB
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Create VLANs on Switch
url = "https://192.168.10.1/restconf/data/Cisco-IOS-XE-native:native/vlan/"
user = "cisco"
pwd = "cisco"
headers = {"Accept":"application/yang-data+xml", "Content-Type":"application/yang-data+xml"}
payload = """<vlan xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<vlan-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan">
<id>10</id>
<name>DATA</name>
</vlan-list>
<vlan-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan">
<id>20</id>
<name>VoIP</name>
</vlan-list>
<vlan-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan">
<id>30</id>
<name>MGMT</name>
</vlan-list>
</vlan>
"""
try:
    response = requests.request("PATCH", url=url, auth=HTTPBasicAuth(user,pwd), headers=headers,
                                data=payload, verify=False)
    if response.status_code in (200,201,204):
        print(f"Success configured Vlans: {response.status_code}")
    else:
        print(f"Failed: {response.status_code}")
except requests.exceptions.HTTPError as error:
    print(f"RESTCONF request failed: {error}")

    if response.text:
        print(response.text)

except requests.exceptions.RequestException as error:
    print(f"Connection failed: {error}")
