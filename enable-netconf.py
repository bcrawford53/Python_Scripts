#Python script that uses netmiko to enable Netconf on Cisco devices
from netmiko import ConnectHandler

#Python Dictionary object to connect to Cisco Devices with Netmiko
device_list = ['192.168.99.128','10.99.254.1','10.99.253.1']
command = ['netconf ssh', 'exit', 'write mem']

#Create a for loop to iterate through device list and connect to each device and enable
# NETCONF
for device in device_list:
    dev_dict = {'device_type': 'cisco_ios',
            'host': device,
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'
                }
    
    
    #Establish SSH session
    try:
        session = ConnectHandler(**dev_dict)

        #Send command to enable NETCONF
        output = session.send_config_set(command)
        print(f"Sending Command to Enable NETCONF on {device}: ")
        print(output)

        #Disconnect session
        session.disconnect()
    except Exception as e:
        print(f"Connection failed on {device}: {e}")

