from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException


csr1 = ConnectHandler(ip = "192.168.60.11", username = "admin", password = "Cisco!@#", device_type = "cisco_xe", session_timeout=120, verbose=True)

csr1_check_connect = csr1.is_alive()

#if str(csr1_check_connect):
#print("\n","CSR1 Connected Successfully!")
#else:
#    print("CSR1 Connecting failed")

csr1.enable()

csr1_configs = csr1.send_config_from_file("csr1.cfg")
print(csr1_configs)
print(" Global Mode: ", csr1.find_prompt())
#csr1.config_mode("config-transaction")
#print(" Configuration Mode: ", csr1.find_prompt())
#cmd = ["interface Loopback 0", "description Configured by Python", "ip address 1.1.1.1 255.255.255.255"]
#output = csr1.send_config_set(cmd, enter_config_mode=True, cmd_verify=True, delay_factor=40, max_loops=250, strip_prompt=True)
csr1.disconnect()
#print(" Device Configured Successfull")
#print("Connection to CSR1: " + str(csr1.disconnect())
