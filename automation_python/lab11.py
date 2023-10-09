import os

intf = [{"int": "interface", "name": "G0/0"}, {"int": "interface", "name": "G0/1"}, {"int": "interface", "name": "G0/2"}, {"desc": "description", "name": "Connected via Python"}, {"cmd": "no", "status": "shut"}]

with open("r1_interfaces.cfg", "w") as modify_intf:
    modify_intf.write(intf[0]["int"] + " " + intf[0]["name"] + "\n")
    modify_intf.write(" " + intf[3]["desc"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(" " + intf[4]["cmd"] + " " + intf[4]["status"] + "\n")

    modify_intf.write(intf[1]["int"] + " " + intf[1]["name"] + "\n")
    modify_intf.write(" " + intf[3]["desc"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(" " + intf[4]["cmd"] + " " + intf[4]["status"] + "\n")

    modify_intf.write(intf[2]["int"] + " " + intf[2]["name"] + "\n")
    modify_intf.write(" " + intf[3]["desc"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(" " + intf[4]["cmd"] + " " + intf[4]["status"] + "\n")

r1_temp = open("r1_interfaces.cfg", "r")
R1 = r1_temp.read()
print(R1)

#os.chdir('/home/n9kway/INE-350-401')
#os.system("cat r1_interfaces.cfg")
