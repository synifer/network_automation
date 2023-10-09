ip_address1 = "10.1.5.5"
temp_ip_address = ip_address1.replace("5", "2")
#print(temp_ip_address)
new_ip_address = temp_ip_address.replace("2", "100", 1)
csr_ip_address = "The IP address of the gateway router is {}"
print("\n", csr_ip_address.format(new_ip_address), "\n")
