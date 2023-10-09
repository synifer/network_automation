import os

vlans = vlans = [{"id": "10", "name": "SERVER"}, {"id": "20", "name": "PC"}, {"id": "30", "name": "VOICE"}, {"id": "40", "name": "Finance"},]


with open("vlans.cfg", "w") as modify_vlans:
    modify_vlans.write("vlan " + vlans[0]["id"] + "\n")
    modify_vlans.write("name " + vlans[0]["name"] + "\n")

    modify_vlans.write("vlan " + vlans[1]["id"] + "\n")
    modify_vlans.write("name " + vlans[1]["name"] + "\n")

    modify_vlans.write("vlan " + vlans[2]["id"] + "\n")
    modify_vlans.write("name " + vlans[2]["name"] + "\n")


os.chdir('/home/n9kway/INE-350-401')
os.system("cat vlans.cfg")
