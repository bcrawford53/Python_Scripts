import requests
from requests.auth import HTTPBasicAuth  
import json

device_list = ['192.168.99.129', '192.168.99.130', '192.168.10.1']
user = 'cisco'
pwd = 'cisco'
headers = {"Accept":"application/yang-data+json", "Content-Type": "application/yang-data+json"}
ospf_payload = {"Cisco-IOS-XE-ospf:router-ospf": {
    "ospf": {
        "process-id": [
            {"id":99,
             "network": [
                 {"ip":"0.0.0.0",
                  "wildcard":"255.255.255.255",
                  "area":0
                  }
             ]}
        ]
    }
}}

for device in device_list:
    url= f"https://{device}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf"

    try:
        response = requests.request("PUT", url=url, auth=HTTPBasicAuth(user,pwd), json=ospf_payload,
                                    headers=headers, verify=False)
        print(f"Success:  {response.status_code}")
        print("\nPayload sent:")
        print(json.dumps(ospf_payload, indent=2))
        print("\nRaw response:")
        print(response.text if response.text else "<empty response>")

        if response.text:
            try:
                print("\nFormatted response:")
                print(json.dumps(response.json(), indent=2))
            except ValueError:
                print("Response was not JSON.")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")