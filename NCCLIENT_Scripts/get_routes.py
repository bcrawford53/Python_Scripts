from ncclient import manager
from ncclient.operations import RPCError
import xml.dom.minidom

dev_list = ['192.168.99.129','192.168.99.130','192.168.10.1']
for device in dev_list:
    try:
        #Connect to device
        print(f"\tConnecting to device: {device}\n")
        if device in ['192.168.99.129','192.168.99.130']:
            with manager.connect(host=device, port=830, username="cisco", password="cisco", timeout=30,
                                device_params={"name":"csr"}, hostkey_verify=False) as m:
                print(f"\tGetting OSPF Config from device: {device}\n")
                rib_filter = """
                <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
                <routing-instance>
                    <name/>
                    <ribs>
                    <rib>
                        <name/>
                        <address-family/>
                        <routes/>
                    </rib>
                    </ribs>
                </routing-instance>
                </routing-state>
                """
                routes = m.get(filter=("subtree",rib_filter))
                print(routes.xml)
                print('\n\n')
                xml_document = xml.dom.minidom.parseString(
                routes.data_xml
                )

                formatted_xml = "\n".join(
                    line
                    for line in xml_document.toprettyxml(
                        indent="  "
                    ).splitlines()
                    if line.strip()
                )

                print(formatted_xml)
        else:
            with manager.connect(host=device, port=830, username="cisco", password="cisco", timeout=30,
                                            device_params={"name":"iosxe"}, hostkey_verify=False) as m:
                print(f"\tGetting OSPF Config from device: {device}\n")
                rib_filter = """
                <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
                <routing-instance>
                    <name/>
                    <ribs>
                    <rib>
                        <name/>
                        <address-family/>
                        <routes/>
                    </rib>
                    </ribs>
                </routing-instance>
                </routing-state>
                """
                routes = m.get(filter=("subtree",rib_filter))
                print(routes.xml)
                print('\n\n')
                xml_document = xml.dom.minidom.parseString(
                routes.data_xml
            )

            formatted_xml = "\n".join(
                line
                for line in xml_document.toprettyxml(
                    indent="  "
                ).splitlines()
                if line.strip()
            )

            print(formatted_xml)
    except RPCError as error:
        print(f"Failed RPC Error: {error}")
    except Exception as e:
        print(f"Failed error: {e}")
