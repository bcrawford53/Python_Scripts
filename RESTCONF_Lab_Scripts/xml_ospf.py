import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

payload =  '''<router xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"  xmlns:ios="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
<ospf>
  <process-id>
    <id>100</id>
    <network>
      <ip>192.168.0.0</ip>
      <wildcard>0.0.255.255</wildcard>
      <area>0</area>
    </network>
  </process-id>
</ospf>
</router-ospf>
</router>
'''

user = "cisco"
pwd ="cisco"
headers = {"Accept":"application/yang-data+xml", "Content-Type":"application/yang-data+xml"}

dev_list = ['192.168.99.129', '192.168.99.130', '192.168.10.1']
for device in dev_list:
    ospf_url = f"https://{device}/restconf/data/Cisco-IOS-XE-native:native/router"
    try:
        print(f"Configuring OSPF on {device}:")
        response = requests.request("PUT", url=ospf_url, auth=HTTPBasicAuth(user,pwd), headers=headers,
                                    data=payload, verify=False)
        if response.status_code in (200,201,204):
            print(f"Success: {response.status_code}")
            if response.text:
                print(response.txt)
    except Exception as e:
        print(f"Failed: {response.status_code}")
