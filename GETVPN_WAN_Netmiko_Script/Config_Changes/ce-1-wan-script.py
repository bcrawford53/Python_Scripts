import os
import yaml
from netmiko import ConnectHandler
from rtr_class import Router

#Open YAML file to grab router and configuration information
with open('ce-1-wan.yaml','r') as file:
    yaml_file = yaml.safe_load(file)


#Create a list of commands to configure the VRF
vrf_commands = [f"vrf definition {yaml_file['vrf']['name']}",
                f"rd {yaml_file['vrf']['rd']}",
                f"route-target both {yaml_file['vrf']['rt_import']}",
                "address-family ipv4",
                "exit"]

#Create a list of commands to configure the Interface
intf_commands = [f"interface {yaml_file['ip_address']['interfaces'][0]['interface']}",
                 f"description {yaml_file['ip_address']['interfaces'][0]['description']}",
                f"vrf forwarding {yaml_file['ip_address']['interfaces'][0]['vrf']}",
                f"ip address {yaml_file['ip_address']['interfaces'][0]['address']} {yaml_file['ip_address']['interfaces'][0]['mask']}",
                "no shutdown",
                "exit",
                f"interface {yaml_file['ip_address']['interfaces'][1]['interface']}",
                f"description {yaml_file['ip_address']['interfaces'][1]['description']}",
                f"ip address {yaml_file['ip_address']['interfaces'][1]['address']} {yaml_file['ip_address']['interfaces'][1]['mask']}",
                "exit"]

#BGP Configuration
bgp_commands = [f"router bgp {yaml_file['bgp']['as_number']}",
                f"address-family ipv4 vrf {yaml_file['bgp']['vrf']}",
                f"neighbor {yaml_file['bgp']['neighbors'][0]['ip']} remote-as {yaml_file['bgp']['neighbors'][0]['remote_as']}",
                "end"]

#Create Router object for Netmiko
RTR_1 = Router(user="cisco", password="cisco", device_type="cisco_ios", host=yaml_file['host'], secret="cisco")
session = RTR_1.connectToDevice()
vrf_output = RTR_1.sendCommandSet(session, vrf_commands)
intf_output = RTR_1.sendCommandSet(session, intf_commands)
bgp_output = RTR_1.sendCommandSet(session, bgp_commands)   

print(vrf_output)
print('*' * 50)
print(intf_output)
print('*' * 50)
print(bgp_output)
print('*' * 50)

