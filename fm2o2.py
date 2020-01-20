import glob
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

path = r"C:\Users\shamb\Desktop\dita_demo"
valid_path = r"C:\Users\shamb\Desktop\dita_demo_scrubbed"

wildcard = "*.xml"
full_path = os.path.join(path, wildcard)

os.makedirs(valid_path, exist_ok=True)

file_list = glob.glob(full_path)

print("The file set includes:")
for this_file in file_list:
    print(this_file)

    # mydoc = minidom.parse(this_file)
    # print(type(mydoc))

    tree = ET.parse(this_file)
    root = tree.getroot()

    print('\nAll item data:')
    for elem in root:
        for subelem in elem:
            print(subelem.text)