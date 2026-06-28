from ncclient import manager
from ncclient.operations import RPCError
import os

try:
    with manager.connect(host="192.168.99.128", port=830, username="cisco", password="cisco",
                         timeout=30, device_params={'name':'iosxe'}, hostkey_verify=False) as m:
        print("Connected to device")
        for capability in m.server_capabilities:
            print(capability)
except RPCError as rpc_error:
    print(f"RPC Error: {rpc_error}")
except Exception as error:
    print(f"Connection/Error: {error}")