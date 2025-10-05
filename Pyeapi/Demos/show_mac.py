import pyeapi

pyeapi.load_config("./eapi.conf")
#Establish a eapi connection to the device
connect = pyeapi.connect_to("a-spine1")

#Send command "show mac address-table" to the device
#The result is a list (cmd_result) with dictinoaries inside

cmd_result = connect.enable("show mac address-table")
print(cmd_result)