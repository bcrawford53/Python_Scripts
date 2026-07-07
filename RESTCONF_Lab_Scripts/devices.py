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