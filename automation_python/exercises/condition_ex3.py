dict1 = {"hostname": "R1", "os": "IOS-XE", "mgmt-ip": "10.1.1.1"}

if dict1["os"] == "IOS-RE":
    print(dict1["mgmt-ip"])
else:
    print("\n" + "The device does not run IOS-XE")
