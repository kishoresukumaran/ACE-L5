import pyeapi
import yaml

pyeapi.load_config('eapi.conf')

file = open('interfaces.yml', 'r')
ip_dict = yaml.safe_load(file)

switches = ['a-host1', 'a-host2']

for switch in switches:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    interface_api = connect.api('ipinterfaces')
    for interface in ip_dict['devices'][switch]['interfaces']:
        ip = ip_dict['devices'][switch]['interfaces'][interface]['ip']
        mask = ip_dict['devices'][switch]['interfaces'][interface]['mask']
        mask = str(mask)
        ip_mask = ip + '/' + mask
        interface_api.create(interface)
        interface_api.set_address(interface, ip_mask)