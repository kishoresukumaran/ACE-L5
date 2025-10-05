import pyeapi

import os

pyeapi.load_config('eapi.conf')

directory = 'configs'
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

switches = ['a-spine1', 'a-spine2', 'a-leaf1', 'a-leaf2', 'a-leaf3', 'a-leaf4', 'a-host1', 'a-host2']

for switch in switches:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    running_config = connect.get_config(as_string='True')
    file = open(f'{directory}/{switch}.cfg', 'w')
    file.write(running_config)
    file.close()
    print(f"Config for {switch} saved to {directory}/{switch}.cfg")