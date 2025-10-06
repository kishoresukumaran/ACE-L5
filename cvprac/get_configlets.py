from cvprac import cvp_client as cvp_client
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = '10.243.248.99'
cvp2 = '10.243.248.100'
cvp3 = '10.243.248.119'
cvp_user = 'cvpadmin'
cvp_password = 'adminadmin'

client = cvp_client.CvpClient()
client.connect([cvp1, cvp2, cvp3], cvp_user, cvp_password)

directory = 'configlets'
if not os.path.exists(directory):
    os.makedirs(directory)

configlets = client.api.get_configlets(start=0,end=5)

for item in configlets['data']:
    file = open(directory + '/' + item['name'] + '.txt', 'w')
    file.write(item['config'])
    file.close()