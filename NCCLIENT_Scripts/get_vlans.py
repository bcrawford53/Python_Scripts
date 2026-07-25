from ncclient import manager
from ncclient.operations import RPCError
import xml.dom.minidom

hostname = "Internal Switch"
IP = "192.168.10.1"

try:
    #Connect to Device
    print(f'Connecting to device {hostname} at ip: {IP}\n')
    vlan_filter = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <vlan>
        <vlan-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan"/>
    </vlan>
    </native>
    """
    with manager.connect(host=IP, port=830, username="cisco", password="cisco", timeout=30,
                         device_params={"name":"iosxe"}, hostkey_verify=False) as m:
        vlan_response = m.get( filter=("subtree", vlan_filter))
        print(f"{hostname} VLAN List:\n")
        print(xml.dom.minidom.parseString(vlan_response.data_xml).toprettyxml())

except Exception as e:
    print(f"Failure because of {e}")