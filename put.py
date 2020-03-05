import json
import requests
from base64 import b64encode
from symbol import if_stmt
requests.urllib3.disable_warnings()

# remplacer adresse IP avec celle de votre routeur
api_url = 'https://172.16.0.34:443/restconf/data/Cisco-IOS-XE-native:native/'


# remplacer root:root par username:password
usrPass = b"python:python"

b64Val = b64encode(usrPass).decode("ascii")

headers = {
    'Accept': "application/yang-data+json",
    'Authorization': "Basic %s" % b64Val,
    'Content-Type': "application/yang-data+json",
    }

payload = {
    "native": {
      "ip": {
        "vrf": {
          "name": "tamer"
        }
      }
    }
}

resp = requests.patch(api_url, headers=headers, data=json.dumps(payload), verify=False)
print("request status: ", resp.status_code)
