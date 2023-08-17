import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("tag1")

# Create and append subelements
sub2 = ET.SubElement(root, "tag2")
sub2.text = "Animal"

sub3 = ET.SubElement(root, "tag3")
sub3.text = "Domestic"

sub4 = ET.SubElement(root, "tag4")
sub4_1 = ET.SubElement(sub4, "tag4.1")
sub4_1.text = "Cat"
sub4_2 = ET.SubElement(sub4, "tag4.2")
sub4_2.text = "Persian"

sub5 = ET.SubElement(root, "tag5")
sub5.text = "Iran"

sub6 = ET.SubElement(root, "tag6")
sub6.text = "Male"

sub7 = ET.SubElement(root, "tag7")
sub7.text = "2021.05.04"

# Print the XML structure using dump()
ET.dump(root)
