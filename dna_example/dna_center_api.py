#!/usr/bin/env python
import requests
import time
from requests.auth import HTTPBasicAuth
from pprint import pprint as pp

base_url = "https://sandboxdnac.cisco.com"
username = "devnetuser"
password = "Cisco123!"

header = {'content-type': 'application/json'}

# Authneticaiton Token
# To disable urllib3 warning:
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
response = requests.post(base_url + '/dna/system/api/v1/auth/token',
                         auth=HTTPBasicAuth(username, password),
                         headers=header, verify=False)

token = response.json()['Token']

# Get device information
header = {'content-type': 'application/json', 'x-auth-token': token}
response = requests.get(base_url + '/dna/intent/api/v1/network-device',
                        headers=header,
                        verify=False)

for device in response.json()['response']:
    try:
        pp(f"Device: {device['id']} - Family: {device['family']}")
    except:
        print('Unable to retrieve id or family')

# Add a new device
new_device = {
    "ipAddress": ["192.0.2.1"],
    "snmpVersion": "v2",
    "snmpROCommunity": "readonly",
    "snmpRWCommunity": "readwrite",
    "snmpRetry": "1",
    "snmpTimeout": "60",
    "cliTransport": "ssh",
    "userName": "cisco",
    "password": "secret123!",
    "enablePassword": "secret456!",
}

# new_device -> body
response = requests.post(base_url + "/dna/intent/api/v1/onboarding/pnp-device",
                         json=new_device,
                         headers=header)

if response.ok:
    time.sleep(10)
    task_id = response.json()["response"]["taskId"]
    task_response = requests.get(base_url + "/intent/api/v1/task/{task_id}",
                            headers=header)

    if task_response.ok:
        task_data = task_response.json()["response"]
        if not task_data["isError"]:
            print("New device successfully added!")
        else:
            print("Async task error seen: {}".format(task_data["progess"]))
    else:
        print("Async GET failed: status code {}".format(task_response.status_code))

else:
    print("Device addition failed with code: {}".format(response.status_code))
    print("Failure body: {}".format(response.text))