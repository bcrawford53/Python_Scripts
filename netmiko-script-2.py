from netmiko import ConnectHandler

USR = "cisco"
PWD = "cisco"
DEV_TYPE = "cisco_ios"

device_list = ["192.168.99.129", "192.168.99.130"]


class Router:
    def __init__(self, user=USR, password=PWD, device_type=DEV_TYPE, secret=PWD, host=""):
        self.device_dict = {
            "device_type": device_type,
            "host": host,
            "username": user,
            "password": password,
            "secret": secret,
        }

    def connect_to_device(self):
        session = ConnectHandler(**self.device_dict)
        session.enable()
        return session

    def send_show_command(self, session, command):
        output = session.send_command(command, read_timeout=120)
        return output

    def send_config_commands(self, session, commands):
        output = session.send_config_set(commands)
        return output


# Create router object
CPE_1 = Router(host=device_list[0])

# Connect to device
sess = CPE_1.connect_to_device()

# Send show command
output = CPE_1.send_show_command(sess, "show running-config")

print(output)

# Disconnect when finished
sess.disconnect()
