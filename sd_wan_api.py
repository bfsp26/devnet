#!/usr/bin/env python3
import requests
import pprint

base_url = "https://sandbox-sdwan-1.cisco.com"
username = "devnetuser"
password = "RG!_Yw919_83"

# start autehtnicated session
# Version 19 and later requires XSRF Token
session = requests.session()
response = session.post(url=base_url + "/j_security_check",
                        data={"j_username": username, "j_password": password},
                        verify=False
                        )

# GET option for device list
device_url = base_url + '/dataservice/device'
device_list = session.get(url=device_url, verify=False)
for device in device_list:
    pprint.pprint(device)
