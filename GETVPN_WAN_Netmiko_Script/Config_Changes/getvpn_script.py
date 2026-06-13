import os
from netmiko import ConnectHandler
from rtr_class import Router

#Create Router object for Netmiko
CUST_WAN_1 = Router(user="cisco", password="cisco", device_type="cisco_ios", host="192.168.254.1", secret="cisco")
CUST_WAN_2 = Router(user="cisco", password="cisco", device_type="cisco_ios", host="192.168.254.2", secret="cisco")
CUST_WAN_3 = Router(user="cisco", password="cisco", device_type="cisco_ios", host="192.168.254.3", secret="cisco")
KEYSERVER = Router(user="cisco", password="cisco", device_type="cisco_ios", host="192.168.254.4", secret="cisco")

WAN_1_COMM_LIST = CUST_WAN_1.openCommandFile('ce1-config.txt')
WAN_2_COMM_LIST = CUST_WAN_2.openCommandFile('ce2-config.txt')
WAN_3_COMM_LIST = CUST_WAN_3.openCommandFile('ce3-config.txt')
KEYSERVER_COMM_LIST = KEYSERVER.openCommandFile('keyserver-config.txt')

WAN_1_OUTPUT = CUST_WAN_1.sendCommandSet(CUST_WAN_1.connectToDevice(), WAN_1_COMM_LIST)
WAN_2_OUTPUT = CUST_WAN_2.sendCommandSet(CUST_WAN_2.connectToDevice(), WAN_2_COMM_LIST)
WAN_3_OUTPUT = CUST_WAN_3.sendCommandSet(CUST_WAN_3.connectToDevice(), WAN_3_COMM_LIST)
KEYSERVER_OUTPUT = KEYSERVER.sendCommandSet(KEYSERVER.connectToDevice(), KEYSERVER_COMM_LIST)

print(WAN_1_OUTPUT)
print('*' * 50)
print(WAN_2_OUTPUT)
print('*' * 50)
print(WAN_3_OUTPUT)
print('*' * 50)
print(KEYSERVER_OUTPUT)
