from netmiko import ConnectHandler

class Router:
    def __init__(self, user, password, device_type, secret, host):
        self.device_dict = {"device_type": device_type,
                            "host": host,
                            "username": user,
                            "password": password,
                            "secret": secret }
    
    #Netmiko function to SSH to device
    def connectToDevice(self):
        session = ConnectHandler(**self.device_dict)
        session.enable()
        return session
    
    #Netmiko method to send a command
    def sendCommand(self, session, command):
        command_output = session.send_command(command)
        return command_output
    
    #Method to send multiple commands, object will need to be a list
    def sendCommandSet(self,session, command_list):
        list_output = session.send_config_Set(command_list)
        return list_output

if __name__ == "__main___":
    print("This is a script for my Router class!")