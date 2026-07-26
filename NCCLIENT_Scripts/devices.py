DEVICES = {"WAN-A":{"ip":"192.168.99.129","usr":"cisco","passwd":"cisco","interfaces":
                    {"GigabitEthernet2": {"name":"2","ip":"192.168.10.2","mask":"255.255.255.0"}}},
           "WAN-B":{"ip":"192.168.99.130","usr":"cisco","passwd":"cisco","interfaces":
                   {"GigabitEthernet2": {"name":"4","ip":"192.168.9.2","mask":"255.255.255.0"}}}}

SWITCHES = {"SWITCH_A": {"ip":"192.168.99.155",
                        "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"CAMERA"}]},
            "SWITCH_B": {"ip":"192.168.99.113",
                         "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"CAMERA"}]}
}

SWITCH_SM_LAB = {"host": "INT_Switch", "ip": "192.168.10.1", "username": "cisco", "password": "cisco",
                  "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"MGMT"}],
                  "routed-vlans": [{"vlan10": 
                                    {"ip":"10.10.10.1", "mask":24} },
                                    {"vlan20":
                                     {"ip":"10.10.20.1", "mask":24}},
                                     {"vlan30":
                                      {"ip":"10.10.30.1", "mask":24}}],
                  "host_interfaces": [{"HOST_A": {"interface": "GigabitEthernet1/0/10", "vlan": 10}},
                                       {"HOST_B": {"interface": "GigabitEthernet1/0/11", "vlan": 20}
                                      }]
                  , "route_interface": {"interface": "GigabitEthernet1/0/1", "switchport": False, "ip": "192.168.20.1",
                                         "mask": 30}}