from netmiko import ConnectHandler
import os

#Login information Its better to hide credentials in environment and pull into the program
USR = "cisco"
PWD = "cisco"
DEV_TYPE = "cisco_ios"

#Devices that will be configured
device_list = ["192.168.99.129", "192.168.99.130"]

#Router class creation that will hold the attributes needed for Netmiko to use to SSH into
#Network equipment
class Router:
    def __init__(self, user=USR, password=PWD, device_type=DEV_TYPE, secret=PWD, host=""):
        self.device_dict = {
            "device_type": device_type,
            "host": host,
            "username": user,
            "password": password,
            "secret": secret,
        }
    #Method uses Netmiko to SSH into device and returns the session
    def connect_to_device(self):
        session = ConnectHandler(**self.device_dict)
        session.enable()
        return session

    #Method used to send a command to the device and returns the vty screen output
    def send_show_command(self, session, command):
        output = session.send_command(command, read_timeout=120)
        return output
    
    #Method used to send a list of commands to the device and returns the vty screen output
    def send_config_commands(self, session, commands):
        output = session.send_config_set(commands)
        return output


# Create router object
CPE_1 = Router(host=device_list[0])

# Connect to device
sess = CPE_1.connect_to_device()

#Commands that will be entered into device are held in text files
list_of_commands = ['ce-1-wan-config.txt', 'ce-2-wan-config.txt', 'ce-3-wan-config.txt']
#Iterate through list to grab the commands to send
for file in list_of_commands:
    command_list = []
    with open(rf'/home/crawford/Automation/Python_Scripts/GETVPN_WAN_Netmiko_Script/{file}','r') as fh:
        file_list = fh.readlines()
    for command in file_list:
        if '---Config for' in command:
            continue
        else:
            command_list.append(command.strip())
    #Send

# Send show command
output = CPE_1.send_config_commands(sess, command_list)

#Display output to the console
print(output)

# Disconnect when finished
sess.disconnect()
