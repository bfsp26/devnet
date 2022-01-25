#|/usr/env/bin python
import xml.etree.ElementTree as ET
from pprint import pprint as pp

# Import data
tree = ET.parse('NX-API_show_version.xml')

# Get root element
root = tree.getroot()
pp("Root tag: {}".format(root.tag))

# Loop over children nodes and print their tag and text
pp("*" * 30)
for child in root:
  tag = child.tag
  text = child.text
  pp(f"tag: {tag}, text: {text}")

# Iterate over output element
pp("*" * 30)
for item in root[3][0]:
    tag, text = item.tag, item.text
    pp(f"tag: {tag}, text: {text}")

# Use findall
pp("*" * 30)
for output in root[3].findall("output"):
  # nested elements -> linear
  for element in output.iter():
    pp(element.tag)