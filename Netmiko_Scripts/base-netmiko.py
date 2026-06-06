from netmiko import ConnectHandler
#Dictornary object with variables and values used to Connect to Cisco Device
device = { "device_type": "cisco_ios",
          "host": HOSTIP,
           "username": USERNAME,
            "password": PASSWD,
             "secret": ENABLE_PWD }

#Try to Connect to Device
try:
    #Establish SSH session
    session = ConnectHandler(**device)

    #Enter Enable mode on device
    session.enable()

    #Send command
    output = connection.send_command(commandarg)

    #Display the output
    print(output)

    #Disconnect the session
    session.disconnect()

except Exception as e:
    print(f"Connection failed: {e}")
