DEVICES = {"rtr1":{"ip":"192.168.99.128","usr":"cisco","passwd":"cisco","interfaces":
                   {"GigabitEthernet4": {"name":"4","ip":"192.168.100.1","mask":"255.255.255.0"},
                    "GigabitEthernet2": {"name":"2","ip":"192.168.90.2","mask":"255.255.255.0"}}},
           "rtr2":{"ip":"192.168.99.129","usr":"cisco","passwd":"cisco","interfaces":
                   {"GigabitEthernet4": {"name":"4","ip":"192.168.100.2","mask":"255.255.255.0"},
                    "GigabitEthernet2": {"name":"2","ip":"192.168.90.1","mask":"255.255.255.0"}},}}

SWITCHES = {"SWITCH_A": {"ip":"192.168.99.155",
                        "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"CAMERA"}]},
            "SWITCH_B": {"ip":"192.168.99.113",
                         "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"CAMERA"}]}
}

SWITCH_SM_LAB = {"host": "INT_Switch", "ip": "192.168.10.1", "username": "cisco", "password": "cisco",
                  "vlans": [{"id":10,"name":"DATA"},{"id":20,"name":"VoIP"},{"id":30,"name":"MGMT"}],
                  "host_interfaces": [{"HOST_A": {"interface": "GigabitEthernet1/0/10", "vlan": 10}},
                                       {"HOST_B": {"interface": "GigabitEthernet1/0/11", "vlan": 20}
                                      }]
                  , "route_interface": {"interface": "GigabitEthernet1/0/1", "switchport": False, "ip": "192.168.20.1",
                                         "mask": 30}}