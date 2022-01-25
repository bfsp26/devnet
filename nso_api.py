#!/usr/bin/env python3
import requests
from pprint import pprint as pp

base_url = 'https://sandbox-nso-1.cisco.com'
username = 'developer'
password = 'Services4Ever'


# Reference the API Docs
# https://developer.cisco.com/docs/nso/#!cisco-nso-swagger-api-docs

# Get device
get_device_url = base_url + '/restconf/data/tailf-ncs:devices/device'

headers = {'Content-Type': 'application/yang-data+json'}

response = requests.get(get_device_url,
                        auth=(username, password),
                        headers=headers,
                        verify=False)

pp(response.text)
