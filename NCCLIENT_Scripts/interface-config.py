from ncclient import manager
from ncclient.operations import RPCError
import xml.dom.minidom
from devices import DEVICES

user = "cisco"
pwd = "cisco"
dev_list = ['192.168.99.129', '192.168.99.130']
WAN_A_IP = DEVICES['WAN-A']['interfaces']['GigabitEthernet2']['ip']
WAN_A_MASK = DEVICES['WAN-A']['interfaces']['GigabitEthernet2']['mask']
WAN_B_IP = DEVICES['WAN-B']['interfaces']['GigabitEthernet2']['ip']
WAN_B_MASK = DEVICES['WAN-B']['interfaces']['GigabitEthernet2']['mask']

get_intf_filter = """<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <GigabitEthernet>
    <name></name>
    <ip>
    <address>
    <primary>
      <address></address>
      <mask></mask>
    </primary>
  </address>
    </ip>
    </GigabitEthernet>
    </interface>
    </native>
"""
for device in dev_list:
    try:
        with manager.connect(host=device, port=830, username=user, password=pwd, timeout=30, device_params={"name":"csr"}, hostkey_verify=False) as m:
            if device == "192.168.99.129":
                print(f"Connecting to device: {device}\nAdding IP Address to G2:\n\n")
                config_intf_filter = f"""<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                    <GigabitEthernet>
                        <name>2</name>
                        <ip>
                        <address>
                        <primary>
                        <address>{WAN_A_IP}</address>
                        <mask>{WAN_A_MASK}</mask>
                        </primary>
                    </address>
                        </ip>
                        </GigabitEthernet>
                        </interface>
                        </native>
                        </config>
                        """
                intf_config_output = m.edit_config(target="candidate", config=config_intf_filter, error_option="rollback-on-error")
            else:
                print(f"Connecting to device: {device}\nAdding IP Address to G2:\n\n")
                config_intf_filter = f"""<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                    <GigabitEthernet>
                        <name>2</name>
                        <ip>
                        <address>
                        <primary>
                        <address>{WAN_B_IP}</address>
                        <mask>{WAN_B_MASK}</mask>
                        </primary>
                    </address>
                        </ip>
                        </GigabitEthernet>
                        </interface>
                        </native>
                        </config>
                        """
                intf_config_output = m.edit_config(target="candidate", config=config_intf_filter, error_option="rollback-on-error")
                
            m.commit()
            print(f"Connecting to device: {device}\nGetting Interface Stats After Change")
            intf_config = m.get(filter=("subtree", get_intf_filter))
            #print the output
            print(xml.dom.minidom.parseString(intf_config.data_xml).toprettyxml())

    except Exception as e:
        print(f"Failed because of error: {e}")