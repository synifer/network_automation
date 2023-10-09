import json


dict1 = {"hostname": "R1",
        "mgmt-ip": "10.1.1.1",
        "username": "rohit",
        "password": "cisco"}
dict2 = {"hostname": "R2",
        "mgmt-ip": "10.1.1.2",
        "username": "rohit",
        "password": "cisco"}
interface_r1 = {"interface": "G1",
        "ip-address": "192.168.1.1"}
interface_r2 = {"interface": "G1",
        "ip-address": "192.168.1.2"}
data_center = [dict1, dict2]
data_center[0]["interface"] = interface_r1
data_center[1]["interface"] = interface_r2

print(json.dumps(data_center, indent=4))
