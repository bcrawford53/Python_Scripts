from netmiko import ConnectHandler
import os

#Login information Its better to hide credentials in environment and pull into the program
USR = "cisco"
PWD = "cisco"
DEV_TYPE = "cisco_ios"

#Devices that will be configured
device_list = ["192.168.99.129", "192.168.99.130", "192.168.99.131"]

#Files for the commands that will be entered into device are held in text files
list_of_commands = ['ce-1-wan-config.txt', 'ce-2-wan-config.txt', 'ce-3-wan-config.txt']

#Router class creation that will hold the attributes needed for Netmiko to use to SSH into
#Network equipment
class Router:
    def __init__(self, user=USR, password=PWD, device_type=DEV_TYPE, secret=PWD, host="", command_list=[], file=""):
        self.device_dict = {
            "device_type": device_type,
            "host": host,
            "username": user,
            "password": password,
            "secret": secret,
        }
        self.command_list = command_list
        self.file = file
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
    def send_config_commands(self, session, command_list=[]):
        output = session.send_config_set(command_list)
        return output
    
    #method will pull the commands from a text file
    def pull_commands_from_file(self):
        try:
            with open(self.file,'r') as fh:
                file_list = fh.readlines()
            for command in file_list:
                self.command_list.append(command.strip())
            return self.command_list
        except FileNotFoundError:
            print(f"File not found: {self.file}")
            return self.command_list


# Create router object
CPE_1 = Router(host=device_list[0], file=list_of_commands[0])
CPE_2 = Router(host=device_list[1], file=list_of_commands[1])  
CPE_3 = Router(host=device_list[2], file=list_of_commands[2])

#List will hold all the objects of network devices to connect to and loop through each and send the commands
device_objects = [CPE_1, CPE_2, CPE_3]
for device in device_objects:
    sess = device.connect_to_device()
    print("*" * 10, f"Connecting to Device: {device.device_dict['host']}", "*" * 10)
    list_output = device.pull_commands_from_file()
    print("This is the list of commands: \n")
    print(list_output)
    output = device.send_config_commands(sess, list_output)
    print("*"*30)
    print(f"Output from device: {device.device_dict['host']} \n")
    print(output)
    print("*"*30)
    sess.disconnect()
    list_output.clear()
