def get_ip(temp):
    dict1 = {"hostname": "R1", "os": "IOS-XE", "mgmt-ip": "10.1.1.1"}
    if temp in dict1["os"]:
        print(dict1["mgmt-ip"])
    else:
        print("The device does not run IOS-XE")


