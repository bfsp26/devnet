#|/usr/env/bin python
import yaml
from pprint import pprint as pp

document = """
---
a: 1
b: String
c:
  d: 3
  e: 5
  f:
    - 5
      6
      7
"""

# From YAML object to Python
yaml_to_python = yaml.load(document, Loader=yaml.FullLoader)
pp(type(yaml_to_python))
pp(yaml_to_python)

# Decode Python to YAML
python_to_yaml = yaml.dump(yaml_to_python)
pp(python_to_yaml)

# Decode YAML to Python object
with open("data/Ansible_Network_Facts_demos.yaml", "r") as yaml_file:
  ansible_playbook = yaml.load(yaml_file.read(), Loader=yaml.FullLoader)

pp(type(ansible_playbook))
pp(ansible_playbook)