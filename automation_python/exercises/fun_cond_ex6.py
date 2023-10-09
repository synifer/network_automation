

device = ["R1", "R2", "SW1", "SW2", "FW1"]

intf = ["GigabitEthernet0/1", "Loopback0", "G0/2", "T1/1/1", "vlan100"]

for item in intf:
    if item.lower().startswith("gig") or item.lower().startswith("g"):
        int_type = "GigabitEthernet"
    elif item.lower().startswith("loop"):
        int_type = "Loopback"
    elif item.lower().startswith("vlan"):
        int_type = "VLAN"
    else:
        int_type = "Unknown"
    print(f"The interface type of {item} is {int_type}")
