# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
import requests
import json
ip = requests.get('https://api.ipify.org?format=json').json()

print(ip)

with open('public_ip.json', 'w') as outfile:
    json.dump(ip, outfile)
