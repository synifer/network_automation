# importing the psutil library  
import psutil  
  
print( "Network Information")  
  
# getting all network interfaces (virtual and physical)  
ifAddrs = psutil.net_if_addrs()  
for interfaceName, interfaceAddresses in ifAddrs.items():  
    for address in interfaceAddresses:  
        print(" Interface: ", interfaceName)  
        if str(address.family) == 'AddressFamily.AF_INET':  
            print("  IP Address: ", address.address)  
            print("  Netmask: ", address.netmask)  
            print("  Broadcast IPv4: ", address.broadcast)  
        elif str(address.family) == 'AddressFamily.AF_PACKET':  
            print("  MAC Address: {address.address}")  
            print("  Netmask: {address.netmask}")  
            print("  Broadcast MAC: {address.broadcast}")  
        elif str(address.family) == 'AddressFamily.AF_INET6':  
            print("  IP Address: ", address.address)  
            print("  Netmask: ", address.netmask)  
            print("  Broadcast IPv6: ", address.broadcast)  
