import pyeapi

pyeapi.load_config('eapi.conf')

switches = ['a-spine1', 'a-spine2', 'a-leaf1', 'a-leaf2', 'a-leaf3', 'a-leaf4', 'a-host1', 'a-host2']
switchess = ['a-spine1']

for switch in switchess:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    vlans_list = connect.enable(['show vlan', 'show version'])
    print(vlans_list[1]['result']['version'])