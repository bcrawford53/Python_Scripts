import os
import yaml
from netmiko import ConnectHandler
import rtr_class

#Open YAML file to grab router and configuration information
with open('ce-1-wan.yaml','r') as file:
    yaml_file = yaml.safe_load(file)


#Create a list of commands to configure the VRF
vrf_commands = [f'vrf definition {yaml_file['vrf']['name']}',
                f'rd {yaml_file['vrf']['rd']}',
                f'route-target both {yaml_file['vrf']['rt_import']}'
                'address-family ipv4',
                'exit']

#Create a list of commands to configure the Interface
intf_commands = [f'interface {yaml_file['ip_address']['interfaces'][0]['interface']}',
                 f'description {yaml_file['ip_address']['interfaces'][0]['description']}',
                f'vrf forwarding {yaml_file['ip_address']['interfaces'][0]['vrf']}',
                f'ip address {yaml_file['ip_address']['interfaces'][0]['address'], yaml_file['ip_address']['interfaces'][0]['mask']}',
                f'interface {yaml_file['ip_address']['interfaces'][1]['interface']}',
                f'description {yaml_file['ip_address']['interfaces'][1]['description']}',
                f'ip address {yaml_file['ip_address']['interfaces'][1]['address'], yaml_file['ip_address']['interfaces'][1]['mask']}',
                ]

#BGP Configuration
bgp_commands = [f'router bgp {yaml_file['bgp']['as_number']}',
                f'address-family ipv4 vrf {yaml_file['bgp']['vrf']}',
                f'neighbor {yaml_file['bgp']['neighbors'][0]['ip']} remote-as {yaml_file['bgp']['neighbors'][0]['remote-as']}',
                'end']

#Create Router object for Netmiko
CE-WAN-1 = rtr_class.Router(user="cisco", password="cisco", device_type="cisco_ios", host=yaml_file['host'])