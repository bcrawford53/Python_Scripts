from ncclient import manager
from ncclient.operations import RPCError
import os

try:
    with manager.connect(host="192.168.99.155", port=830, username="netadmin", password="cisco123",
                         timeout=30, device_params={'name':'iosxe'}, hostkey_verify=False) as m:
        print("Connected to device")
        for capability in m.server_capabilities:
            print(capability)
            capability_list =[]
            capability_list.append(capability)
        with open("capabilities.txt", "a") as f:
            for capability in capability_list:
                f.write(capability + "\n")
except RPCError as rpc_error:
    print(f"RPC Error: {rpc_error}")
except Exception as error:
    print(f"Connection/Error: {error}")