from netmiko import ConnectHandler
import json

user_input = input("Enter Json File name: ")
with open(user_input) as file:
      json_file = file.read()
      json_obj = json.loads(json_file)

#function creation to SSH into device using Netmiko
def Connect_to_Device(device_dict):
        with ConnectHandler(**device_dict) as session:
            return session

#Function create to send commands to device
def Send_Commands(session, command_list):
      output = session.send_command_set(command_list)
      print(output)
      return output

#Iterate through json file that each router is an element in the list
for x in range(len(json_obj)):
    dev_type = json_obj[x]['device_type']
    devIP = json_obj[x]['hostIPaddress']
    usr = json_obj[x]['username']
    pwd = json_obj[x]['password']
    enable_pwd = json_obj[x]['enable_pwd']

    #Need a function or commands to iterate through list and generate a command list????

    device_dict = {"device_type": {dev_type},
            "host": {dev_IP},
            "username": {usr},
            "password": {pwd},
            "secret": {enable_pwd}
    }
    sess_obj = Connect_to_Device(device_dict)





    
