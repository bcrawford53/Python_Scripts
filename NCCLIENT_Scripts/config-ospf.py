from ncclient import manager
from ncclient.operations import RPCError
import xml.dom.minidom

dev_list =['192.168.99.129','192.168.99.130']

for device in dev_list:
    try:
        print(f"\tConnecting to device: {device}\n\tConfiguring OSPF")
        ospf_filter = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
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
            </native>
        </config>
        """

        with manager.connect(host=device, port=830, username="cisco", password="cisco", timeout=30,
                             device_params={"name":"csr"}, hostkey_verify=False) as m:
             ospf_response = m.edit_config(target="candidate", config=ospf_filter,
                                           error_option="rollback-on-error")
             m.commit()

    except RPCError as error:
            print(f"Failed RPC Error: {error}")
    except Exception as e:
        print(f"Failed error: {e}")