import requests
from requests.auth import HTTPBasicAuth
import json

DEVICES = {
    "CSR_A": {"url": "https://192.168.99.128/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=4",
              "usr": "cisco",
              "pwd": "cisco",
              "headers": {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"},
              "payload": {"Cisco-IOS-XE-native:GigabitEthernet": {"description": "Link to CSR_B",
                                                                  "ip":
                                                                    {"address":
                                                                        {"primary":
                                                                            {"address": "192.168.100.253", "mask": "255.255.255.252"}
                                                                            }}}}
    },
    "CSR_B": {"url": "https://192.168.99.129/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=4",
              "usr": "cisco",
              "pwd": "cisco",
              "headers": {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"},
              "payload": {"Cisco-IOS-XE-native:GigabitEthernet": {"description": "Link to CSR_A",
                                                                  "ip":
                                                                    {"address":
                                                                        {"primary":
                                                                            {"address": "192.168.100.254", "mask": "255.255.255.252"}
                                                                            }}}}
    }
}

for device in DEVICES:
    device_info = DEVICES[device]
    url = device_info["url"]
    usr = device_info["usr"]
    pwd = device_info["pwd"]

    headers = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}

    request = requests.get(url, auth=HTTPBasicAuth(usr, pwd), headers=headers, verify=False)

    if request.status_code == 200:
        data = request.json()
        print(f"Device: {device}")
        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {request.status_code}")
        print(request.text)

    change_request = requests.patch(url, auth=HTTPBasicAuth(usr, pwd), headers=headers, verify=False, data=json.dumps(device_info["payload"]))
    if change_request.status_code == 204:
        print(f"Device: {device} - Configuration updated successfully")
    else:
        print(f"Error updating device: {device}")
        print(change_request.text)
    
    #Enable Interface
    shutdown_url = f"{url}/shutdown"
    enable_request = requests.delete(shutdown_url, auth=HTTPBasicAuth(usr, pwd), headers=headers, verify=False)
    if enable_request.status_code == 204:
        print(f"Device: {device} - Interface enabled successfully")
    else:
        print(f"Error enabling interface on device: {device}")
        print(enable_request.text)  
        