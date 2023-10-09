total_routers = 50
total_switches = 100
total_firewalls = 10
total_devices = total_routers + total_switches + total_firewalls
router_version = "IOS-XE"
switch_version = "IOS 15.4"
it_engineers = 4
work_load = total_devices / it_engineers
print(f"There are {total_devices} Devices in our Data Center")
print(f"There are {it_engineers} Engineers work in our DC")
print(f"Total Work Load per Engineer {work_load} Devices")
print("There are", total_routers, "devices running", router_version)
print("There are", total_switches, "device running", switch_version)
