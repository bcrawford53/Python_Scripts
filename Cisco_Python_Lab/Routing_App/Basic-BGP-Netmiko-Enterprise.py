from netmiko import ConnectHandler

#Create Constant Variables for username and password and device type
USR = 'cisco'
PWD = 'cisco'
DEV_TYPE = 'cisco_ios'

#Network devices IPs we are connecting to
device_list = ['192.168.99.129', '192.168.99.130']
COMMANDS = []

#Router Class that will hold attributes used to connect to device and command list
class Router:
    def __init__(self, user=USR, password = PWD, device_type= DEV_TYPE, secret= PWD, host=""):
        self.user = user
        self.password = password
        self.device_type = device_type
        self.secret = secret
        self.host = host
        device_dict = {"device_type": self.device_type, "host": self.host,
                       "username": self.user, "password": self.password,
                       "secret": self.secret}

    def Connect_to_Device(self, device_dict):
        with ConnectHandler(**device_dict) as session:
            return session
    
    def Send_Commands(self, sess, COMMANDS):
        output = sess.send_command_set(COMMANDS)
        return output


# make router objects that will be used to connect to devices
CPE_1 = Router(host=device_list[0])
CPE_2 = Router(host=device_list[1])

sess = CPE_1.Connect_to_Device()
#result = CPE_1.Send_Commands(sess,)