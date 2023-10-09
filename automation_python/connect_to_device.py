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
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    result = output.find('uptime is')
    begin = int(result)
    end = begin + 38
    print(device["ip"] + " => " + output[int(begin):int(end)])

    
#csr1 = ConnectHandler(ip = "192.168.60.11", username = "admin", password = "Cisco!@#", device_type = "cisco_xe")
#csr2 = ConnectHandler(ip = "192.168.60.12", username = "admin", password = "Cisco!@#", device_type = "cisco_xe")

#csr1_check_connect = csr1.is_alive()
#csr2_check_connect = csr2.is_alive()

#if str(csr1_check_connect):
#    print("\n","CSR1 Connected Successfully!")
#else:
#    print("CSR1 Connecting failed")
#if str(csr2_check_connect):
#    print("\n", "CSR2 Connected Successfully!")
#else:
#    print("CSR2 Connecting failed")

#cmd_csr1 = ["interface Loopback 0", "description Configured by Python", "ip address 1.1.1.1 255.255.255.255"]

#cmd_csr2 = ["interface Loopback 0", "description Configured by Python", "ip address 2.2.2.2 255.255.255.255"]
#csr1.enable()
#csr1.config_mode("config-transaction")
#csr2.enable()
#csr2.config_mode("config-transaction")
#output_csr1 = csr1.send_config_set(cmd_csr1)
#output_csr2 = csr2.send_config_set(cmd_csr2)


#csr1.disconnect()
#csr2.disconnect()
