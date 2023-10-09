# Lists
ip_address = "10.1.5.5"
interface = "G0/0/0/0"
list1 = [interface, ip_address, "description connected via Python", "shut"]
print("\n", list1[0])
print("\n", list1[1])
print("\n", list1[2])
print("\n", list1[3])
print("\n", list1)
list1[3] = "no shut"
print("\n", "The IP address of the router is", list1[1], "and the management interface is", list1[0], "\n")
