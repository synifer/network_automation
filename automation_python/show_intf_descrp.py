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
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()
    print(output)
