from netmiko import ConnectHandler
import time

dev_list = ['192.168.99.129','192.168.99.130','192.168.10.1']

for device in dev_list:
    if device == '192.168.99.129':
        print(f"Connecting to Device WAN-A at {device}\n")
        sessionA = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                 password="cisco", secret="cisco")
        print()
        command_list_WANA = ['interface G2', 'descrip LAN Interface', 'ip address 192.168.10.2 255.255.255.0',
                              'exit','router ospf 100','network 192.168.0.0 0.0.255.255 area 0', 'end']
        output_A = sessionA.send_config_set(command_list_WANA)
        print(sessionA.find_prompt(),output_A)
        sessionA.disconnect()
        time.sleep(10)
    elif device == "192.168.99.130":
        print(f"Connecting to Device WAN-B at {device}\n")
        sessionB = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                    password="cisco", secret="cisco")
        print()
        command_list_WANB = ['interface G2', 'descrip LAN Interface', 'ip address 192.168.9.2 255.255.255.0',
                                'exit','router ospf 100','network 192.168.0.0 0.0.255.255 area 0', 'end']
        output = sessionB.send_config_set(command_list_WANB)
        print(sessionB.find_prompt(),output)
        sessionB.disconnect()
        time.sleep(10)
    else:
        print(f"Connecting to Device Internal Switch at {device}\n")
        sessionC = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                    password="cisco", secret="cisco")
        print()
        command_list_Switch = ['vlan 20', 'name DATA', 'exit','interface Vlan 20',
                               'desc DATA VLAN NETWORK', 'ip address 10.20.20.20 255.255.255.0',
                               'exit', 'router ospf 100', 'network 10.20.20.0 0.0.0.255 area 0', 'end']
        outputC = sessionC.send_config_set(command_list_Switch)
        print(sessionC.find_prompt(),outputC)
        sessionC.disconnect()
        time.sleep(10)

time.sleep(10)
for device in dev_list:
    if device == '192.168.99.129':
            print(f"Connecting to Device WAN-A at {device}\n")
            sessionA = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                     password="cisco", secret="cisco")
            print()
            output_A = ""
            output_A = sessionA.send_command('show ip ospf neighbor')
            print(sessionA.find_prompt(),output_A)
            output_A = sessionA.send_command('show ip route')
            print(sessionA.find_prompt(),output_A)
            sessionA.disconnect()
    elif device == "192.168.99.130":
        print(f"Connecting to Device WAN-B at {device}\n")
        sessionB = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                    password="cisco", secret="cisco")
        print()
        output_B = ""
        output_B = sessionB.send_command('show ip ospf neighbor')
        print(sessionB.find_prompt(),output_B)
        output_B = sessionA.send_command('show ip route')
        print(sessionB.find_prompt(),output_B)
        sessionB.disconnect()
    else:
        print(f"Connecting to Device Internal Switch at {device}\n")
        sessionC = ConnectHandler(ip=device, device_type="cisco_ios", username="cisco",
                                    password="cisco", secret="cisco")
        print()
        output_C = ""
        output_C = sessionC.send_command('show ip ospf neighbor')
        print(sessionC.find_prompt(),output_C)
        output_C = sessionC.send_command('show ip route')
        print(sessionC.find_prompt(),output_C)
        sessionC.disconnect()

