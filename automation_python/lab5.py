ccie = "CCIE Enterprise Infrastructure\n CCIE Service Provider\n CCIE Security"
ip_address1 = "10.1.2.100"
ip_address2 = "10.3.4.200"
lower_ccie = ccie.lower()
new_ip_address1 = ip_address1.split(".")
new_ip_address2 = ip_address2.split(".")
new_lower_ccie = lower_ccie.splitlines()

print(new_ip_address1[2])
print(new_ip_address2[3])
print(new_lower_ccie)

