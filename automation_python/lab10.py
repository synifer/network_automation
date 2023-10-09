import os

vlans = [
        {
        "id": "10",
        "name": "DATA"
            },
        {"id": "20",
        "name": "VOICE"},
        {
        "id": "30",
        "name": "MGMT"
            }
        ]
modify_vlans = open("vlans.cfg", "w")

modify_vlans.write("vlan " + vlans[0]["id"] + "\n")
modify_vlans.write("name " + vlans[0]["name"] + "\n")

modify_vlans.write("vlan " + vlans[1]["id"] + "\n")
modify_vlans.write("name " + vlans[1]["name"] + "\n")

modify_vlans.write("vlan " + vlans[2]["id"] + "\n")
modify_vlans.write("name " + vlans[2]["name"] + "\n")

modify_vlans.close()

os.chdir('/home/n9kway/INE-350-401')
os.system("cat vlans.cfg")
