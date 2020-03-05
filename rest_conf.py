import json
import requests
from base64 import b64encode
from symbol import if_stmt
requests.urllib3.disable_warnings()

api_url = 'https://172.16.0.34:443/restconf/data/Cisco-IOS-XE-native:native/'

usrPass = b"python:python"

b64Val = b64encode(usrPass).decode("ascii")

print(b64Val)

headers = {
    'Accept': "application/yang-data+json",
    'Authorization': "Basic %s" % b64Val,
    'Content-Type': "application/yang-data+json",
    }


# Récupère les VRF existant sur le switch Cisco
def get_vrf():
    vrf_url = api_url + 'ip/vrf/'
    resp = requests.get(vrf_url, headers=headers, verify=False)
    print("request status: ", resp.status_code)  # display response code

    if resp.status_code == 200:
        # Create object to contain the converted json-formatted response
        response_json = resp.json()

        # display service ticket value
        print("json data : ", response_json)
    else:
        print(resp)

    for e in response_json['Cisco-IOS-XE-native:vrf']:
        print('There is a vrf named ' + e['name'])


def create_vrf(vrf_name):

    payload = {
        "native": {
            "ip": {
                "vrf": {
                    "name": vrf_name
                }
            }
        }
    }

    resp = requests.get(api_url, headers=headers, data=json.dumps(payload), verify=False)

    print("request status: ", resp.status_code)


# get_vrf()
create_vrf('debilemental')


