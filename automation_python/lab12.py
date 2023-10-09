def device_ip(temp):
        dict1 = {"hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}
        dict2 = {"hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}
        if temp in dict1["OS"] == "IOS-XE":
            print("\n" + "The management IP of", dict1["hostname"], "is", dict1["mgmt-ip"])
        elif temp in dict2["OS"] == "IOS-XR":
            print("\n" + "The management IP of", dict2["hostname"], "is", dict2["mgmt-ip"])
        else:
            print("\n" + "The device has an unknown image")

