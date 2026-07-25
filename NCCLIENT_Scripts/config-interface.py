from ncclient import manager
from ncclient.operations import RPCError
import xml.dom.minidom

dev_list = ['192.168.99.129','192.168.99.130']

#Iterate through device list to connect to each device and get interface configs
for device in dev_list:
    try:
        #connect to device
        with manager.connect(host=device, port=830, username="cisco", 
                         password="cisco", timeout=30, device_params={'name':'csr'},
                         hostkey_verify=False) as m:
            print(f"Connecting to device: {device}\n")
            print("Getting Interface Config.")
            intf_filter = '''<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface/>
            </native>'''
            intf_config = m.get_config(source="running", filter=('subtree', intf_filter))

            #print the XML output
            print(xml.dom.minidom.parseString(intf_config.data_xml).toprettyxml())
            print('\n\n')
    except RPCError as error:
        print(f"Failed RPC Error: {error}")
    except Exception as e:
        print(f"Failed error: {e}")
                                       

