from netmiko import ConnectHandler
from getpass import getpass

#Connect to Internal Switch
#Get username and password
user = input("Enter username for SSH: \n")
pwd = getpass("Enter in SSH password: \n")
ipaddr = input("Enter in the IP address of the switch: ")
switch_dict = {"ip": ipaddr, "device_type": "cisco_ios", "username": user,
               "password": pwd, "secret":"cisco"}
#Connect to Switch
sess = ConnectHandler(**switch_dict)
command_list = ['interface vlan 20', 'ip address 10.20.20.1 255.255.255.0', 
                'exit', 'interface range Gi1/0/10-11', 'switchport host',
                'switchport access vlan 20']
#Send command list to Switch
output = sess.send_config_set(command_list)
print(output)

#Show command to verify config changes
output = sess.send_command('show run int vlan 20')
print('\n',output)
output = sess.send_command('show run int gi1/0/10')
print('\n',output)
output = sess.send_command('show run int gi1/0/11')
print('\n',output)
sess.disconnect()
