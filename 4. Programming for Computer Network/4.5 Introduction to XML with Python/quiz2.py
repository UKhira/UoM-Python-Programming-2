import xml.etree.ElementTree as ET

# Preloaded XML document
vehicle_xml_data_as_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>"

# Parse the XML string
root = ET.fromstring(vehicle_xml_data_as_string)

# Update details for the vehicle with registration number DE2115
for vehicle in root.findall(".//vehicle[registration_no='DE2115']"):
    make_element = vehicle.find("make")
    model_element = vehicle.find("model")

    make_element.text = "Nissan"
    model_element.text = "Skyline"

# Print the updated XML structure
updated_xml_string = ET.tostring(root, encoding="utf-8", method="xml")
print(updated_xml_string.decode("utf-8"))

# Print Registration Numbers of each Nissan vehicle
print("\nRegistration Numbers of Nissan vehicles:")
nissan_vehicles = root.findall(".//vehicle[make='Nissan']")
for vehicle in nissan_vehicles:
    reg_no = vehicle.find("registration_no").text
    print(reg_no)
