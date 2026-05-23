from netmiko import ConnectHandler
import json

#function creation to SSH into device using Netmiko
def Connect_to_Device(device_dict):
        with ConnectHandler(**device_dict) as session:
            return session

#Function create to send commands to device
def Send_Commands(session, command_list):
      output = session.send_command_set(command_list)
      print(output)
      return output

user_input = input("Enter Json File name: ")
with open(user_input) as file:
      json_file = file.read()
      json_obj = json.loads(json_file)

hostnames = []
#Iterate through json file that each router is an element in the list
for device in range(len(json_obj)):
    dev_type = json_obj[device]['device_type']
    devIP = json_obj[device]['hostIPaddress']
    usr = json_obj[device]['username']
    pwd = json_obj[device]['password']
    enable_pwd = json_obj[device]['enable_pwd']
    command_list = json_obj[device]['commands']
    host = json_obj[device]['hostname']
    hostnames.append(host)

    #Need a function or commands to iterate through list and generate a command list????
    device_dict = {"device_type": {dev_type},
            "host": {dev_IP},
            "username": {usr},
            "password": {pwd},
            "secret": {enable_pwd}
    }
    sess_obj = Connect_to_Device(device_dict)
    print(f"*"*10,"Connected to {devIP}","*"*10)

    #Send the commands and print the output
    command_output = Send_Commands(sess_obj, command_list)
    print(command_output)







    
