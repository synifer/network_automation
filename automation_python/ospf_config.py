from netmiko import Netmiko
from netmiko import ConnectHandler


devices = [{
    "device_type": "cisco_xe",
    "ip": "192.168.60.11",
    "username": "admin",
    "password": "Cisco!@#"
    },
    {
    "device_type": "cisco_xe",
    "ip": "192.168.60.12",
    "username": "admin",
    "password": "Cisco!@#"
    }]
for device in devices:
    net_connect = ConnectHandler(**device)
    net_connect.config_mode("config-transaction")
    output = net_connect.send_config_from_file("csr1.cfg")
    net_connect.disconnect()
    print(output)
