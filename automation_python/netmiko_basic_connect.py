
from netmiko import ConnectHandler



devices = { "device_type": "cisco_ios",
            "ip": "192.168.60.11", 
            "username": "admin",
            "password": "cisco",
            "secret": "cisco" } 

commands = ['router ospf 1',
       'network 10.0.0.0 0.255.255.255 area 0',
       'network 192.168.100.0 0.0.0.255 area 1']
ssh = ConnectHandler(**devices)
ssh.enable()
#ospf_config = ssh.send_config_set(commands)
result = ssh.send_command("show running-config")
with open("r1_run_config.cfg", 'a') as file:
    file.write(str(result) + '\n')



