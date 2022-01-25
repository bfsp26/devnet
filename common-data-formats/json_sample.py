#!/usr/bin/env python
import json
from pprint import pprint as pp

pp("Encoding Python objects into JSON")
python_to_json = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
pp(python_to_json)

pp("Decoding JSON objects into Python")
json_to_python = json.loads(python_to_json)
pp(json_to_python)

pp("Read JSON file and turn into Python object:")
with open("NX-API_show_version.json", "r") as json_file:
  show_version_output = json.loads(json_file.read())

pp("Show the type of Python object and content:")
pp(type(show_version_output))
pp(show_version_output)

pp("Parse out the NX-OS version value:")
pp(show_version_output['ins_api']['outputs']['output']['body']['nxos_ver_str'])