import requests
from requests.auth import HTTPBasicAuth
from devices import SWITCH_SM_LAB
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

switch_dict = SWITCH_SM_LAB

user = switch_dict["username"]
pwd = switch_dict["password"]
hostname = switch_dict["host"]

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = (
    f"https://192.168.10.1/restconf/data/"
    "openconfig-interfaces:interfaces/interface=Vlan30/routed-vlan"
)

payload = {
  "openconfig-vlan:routed-vlan": {
    "openconfig-if-ip:ipv4": {
      "addresses": {
        "address": [
          {
            "ip": "10.10.30.1",
            "config": {
              "ip": "10.10.30.1",
              "prefix-length": 24
            }
          }
        ]
      }}}}

try:
    print(f"Creating SVI interface on device: {hostname}")

    response = requests.patch(
        url=url,
        auth=HTTPBasicAuth(user, pwd),
        headers=headers,
        json=payload,
        verify=False,
        timeout=30
    )

    print(f"Status code: {response.status_code}")

    print("\nPayload sent:")
    print(json.dumps(payload, indent=2))

    print("\nActual request body:")
    if isinstance(response.request.body, bytes):
        print(response.request.body.decode())
    else:
        print(response.request.body)

    print("\nResponse:")
    if response.text:
        try:
            print(json.dumps(response.json(), indent=2))
        except ValueError:
            print(response.text)

    response.raise_for_status()

    print("SVI interface configured successfully.")

except requests.exceptions.HTTPError as error:
    print(f"RESTCONF request failed: {error}")

    if response.text:
        print(response.text)

except requests.exceptions.RequestException as error:
    print(f"Connection failed: {error}")