import pyeapi
import yaml

pyeapi.load_config('eapi.conf')

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['devices']:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    vlans_api = connect.api('vlans')
    for item in vlan_dict['vlan_list']:
        vlan_id = item['id']
        vlan_name = item['name']
        print(f"Creating VLAN {vlan_id} with name {vlan_name}")
        vlans_api.create(vlan_id)
        vlans_api.set_name(vlan_id, vlan_name)

