import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES, SWITCH_SM_LAB
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Configure G2 interface with 192.168.9.2/30
try:
    rtr_dict = DEVICES
    intf_url = "https://192.168.99.130/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
    print(f"Attempting to connect to 192.168.99.130")
    headers = {"Accept":"application/yang-data+xml", "Content-Type":"application/yang-data+xml"}
    payload = """<GigabitEthernet xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <name>2</name>
        <ip>
        <address>
        <primary>
            <address>192.168.9.2</address>
            <mask>255.255.255.252</mask>
        </primary>
        </address>
        </ip>
        </GigabitEthernet>
        """.strip()
    response = requests.request("PUT", url=intf_url, auth=HTTPBasicAuth(rtr_dict['WAN-B']['usr'],rtr_dict['WAN-B']['passwd']),
                                headers=headers, data=payload, verify=False)
    if response.status_code in (200,201,204):
        print("Success! Enabled Interface G2 and gave it the IP address of 192.168.9.2/30")
        print(response.status_code)
    else:
        print("Failed to enable the interface!")
except requests.exceptions.HTTPError as error:
    print(f"RESTCONF request failed: {error}")

    if response.text:
        print(response.text)

except requests.exceptions.RequestException as error:
    print(f"Connection failed: {error}")

#Enable Intf Gi1/0/1 on the Switch and give it the IP of 192.168.9.1/30
switch_dict = SWITCH_SM_LAB
user = switch_dict['username']
pwd = switch_dict['password']
switch_url = "https://192.168.10.1/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F1"
switch_payload = """<GigabitEthernet xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
       <name>1/0/1</name>
  <switchport-conf>
    <switchport>false</switchport>
  </switchport-conf>
  <ip>
    <address>
      <primary>
        <address>192.168.9.1</address>
        <mask>255.255.255.252</mask>
      </primary>
    </address>
  </ip>
        </GigabitEthernet>
        """
try:
    switch_response = requests.request("PATCH", url=switch_url, auth=HTTPBasicAuth(user,pwd), headers=headers,
                                       data=switch_payload, verify=False)
    if switch_response.status_code in (200,201,204):
        print("Success added interface to Switch!")
        print(switch_response.status_code)
    else:
        print("Failed to configure switch!")
        print(switch_response.status_code)
except requests.exceptions.HTTPError as error:
    print(f"Failed: {switch_response.status_code},error: {error}")
    if switch_response.text:
        print(switch_response.text)
except requests.exceptions.RequestException as error:
    print(f"Failed: {error}")
    print(switch_response.status_code)