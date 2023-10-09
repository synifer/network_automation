
def device_info(os):

    dev1 = { "hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}
    dev2 = { "hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}
    dev3 = { "hostname": "R3", "OS": "NX-OS", "mgmt-ip": "10.1.1.3"}
    dev4 = { "hostname": "R4", "OS": "IOS-XR", "mgmt-ip": "10.1.1.4"}
    dev5 = { "hostname": "R5", "OS": "NX-OS", "mgmt-ip": "10.1.1.5"}
    device_list = [dev1, dev2, dev3, dev4, dev5]

    for device in device_list:
        for key, value in device.items():
            if value == "IOS-XE" and os == "IOS-XE":
                print("\n", "The management IP for " + device["hostname"], "is " + device["mgmt-ip"])
            elif value == "IOS-XR" and os == "IOS-XR":
                print("\n", "The management IP for " + device["hostname"], "is " + device["mgmt-ip"])
            elif value == "NX-OS" and os == "NX-OS":
                print("\n", "The management IP for " + device["hostname"], "is " + device["mgmt-ip"])
            else:
                pass
                #print("\n", "No device with", os, "name found.")




#device_list = ["dev1": { "hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"},"dev2": { "hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}, "dev1": { "hostname": "R3", "OS": "NX-OS", "mgmt-ip": "10.1.1.3"}]

