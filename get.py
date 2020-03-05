import json
import requests
from base64 import b64encode
from symbol import if_stmt
requests.urllib3.disable_warnings()

# remplacer adresse IP avec celle de votre routeur
#api_url = 'https://172.16.0.121:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F2'
#api_url = 'https://172.16.0.121:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F1'
api_url = 'https://172.16.0.112:443/restconf/data/Cisco-IOS-XE-native:native/ip/vrf/'

# remplacer root:root par username:password
usrPass = b"python:python"

b64Val = b64encode(usrPass).decode("ascii")

headers = {
    'Accept': "application/yang-data+json",
    'Authorization': "Basic %s" % b64Val,
    'Content-Type': "application/yang-data+json",
    }

resp = requests.get(api_url, headers=headers, verify=False)

# Create object to contain the request status
print("request status: ", resp.status_code)  # display response code

if resp.status_code == 200:
    # Create object to contain the converted json-formatted response
    response_json = resp.json()

    # display service ticket value
    print("json data : ", response_json)
else:
    print(resp)

