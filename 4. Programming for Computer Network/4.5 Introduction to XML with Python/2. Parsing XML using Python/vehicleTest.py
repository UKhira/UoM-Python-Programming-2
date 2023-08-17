import xml.etree.ElementTree as ET


file_path = 'C:/Users/user/Documents/GitHub/UoM-Python-Programming-2/4. Programming for Computer Network/4.5 Introduction to XML with Python/vehicle.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# Now you can work with the root element and the XML data

# tree = ET.parse('vehicle.xml')
# root = tree.getroot()