from nacl import encoding
from ncclient import manager
from ncclient.operations import RPCError
from xml.dom import minidom
import os

try:
    with manager.connect(host="192.168.99.128", port=830, username="cisco", password="cisco",
                        timeout=30,device_params={'name':'iosxe'}, hostkey_verify=False) as m:
        print("Connected to device")
        running_config = m.get_config(source="running")
        print(running_config.xml)
        xml_string = running_config.xml

        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="    ")

        print(pretty_xml)

        # Save the pretty XML to a file
        with open("running_config.xml", "w",encoding='utf-8') as f:
            f.write(pretty_xml)

except RPCError as rpc_error:
    print(f"RPC Error: {rpc_error}")

except Exception as error:
    print(f"Connection/Error: {error}")