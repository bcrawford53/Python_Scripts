import requests
from requests.auth import HTTPBasicAuth
from devices import DEVICES


for device, dev_dict in DEVICES.items():
    IP = dev_dict['ip']
    USERNAME = dev_dict['usr']
    PWD = dev_dict['passwd']
    intf_num = dev_dict['interfaces']['GigabitEthernet2']['name']
    intf_ip = dev_dict['interfaces']['GigabitEthernet2']['ip']
    intf_mask = dev_dict['interfaces']['GigabitEthernet2']['mask']
    payload = f"""<GigabitEthernet xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <name>{intf_num}</name>
            <ip>
            <address>
            <primary>
            <address>{intf_ip}</address>
            <mask>{intf_mask}</mask>
            </primary>
        </address>
        </ip>
        </GigabitEthernet>
        """
    url = f"https://{IP}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={intf_num}"
    headers = {"Accept": "application/yang-data+xml", "Content-Type": "application/yang-data+xml"}
    try:
        response = requests.request("PATCH", url=url, auth=HTTPBasicAuth(USERNAME, PWD), headers=headers,
                                    data=payload, verify=False)
        if response.status_code in (200, 201, 204):
            print(f"Success! {response.status_code}")
        else:
            print(f"Configuration Failed -- {response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"RESTCONF request failed: {error}")