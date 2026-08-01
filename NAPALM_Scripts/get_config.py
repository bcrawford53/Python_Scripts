from pprint import pprint
import napalm


device_list = ['192.168.99.129','192.168.99.130']

for device in device_list:
    driver = napalm.get_network_driver("ios")
    router = driver(hostname=device, username="cisco", password="cisco")
    router.open()
    device_dict = router.get_facts()
    print(f"Connected to device {device_dict['hostname']} at: {device}")
    pprint(f"Hostname: {device_dict['hostname']} ----- Version# {device_dict['os_version']}")
    print("\nClosing Connection!\n\n")



