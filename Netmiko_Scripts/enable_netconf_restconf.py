from netmiko import ConnectHandler
import time

device_list = ['192.168.99.129', '192.168.0.2', '192.168.0.6', '192.168.0.10', 
               '192.168.0.14']

#Connect to each device and enable NETCONF and RESTCONF
for device in device_list:
    sess = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                           password="cisco")
    print(f"\tConnect to Device: {device}")
    print("Enabling NETCONF and RESTCONF: \n")
    output = sess.send_config_set(["netconf-yang","netconf-yang feature candidate-datastore",
                                  "restconf", "ip http server", "ip http secure-server",
                                  "ip http authentication local"])
    print(output)
    print("Saving Config:\n")
    sess.save_config()
    sess.disconnect()

time.sleep(15)
#Verify Config 
for device in device_list:
    sess = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                           password="cisco")
    print(f"\tConnect to Device: {device}")
    print("Verify NETCONF and RESTCONF: \n")
    netconf_output = sess.send_command("show netconf-yang status")
    print(netconf_output,"\n")
    restconf_output = sess.send_command("show runn | i restconf")
    print(restconf_output)