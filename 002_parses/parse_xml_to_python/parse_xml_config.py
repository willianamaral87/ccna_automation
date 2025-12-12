# Import Python buit-in XML Parse Library
import xml.etree.ElementTree as ET

# Function to parse from a XML file to Python
def parse_xml_config(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Parse device info
    print("=== Device Information ===")
    device = root.find("Device")
    for elem in device:
        print(f"{elem.tag}: {elem.text}")

    # Parse interfaces
    print("\n=== Interfaces ===")
    interfaces = root.find("Interfaces")
    for interface in interfaces.findall("Interface"):
        print("--- Interface ---")
        for elem in interface:
            print(f"{elem.tag}: {elem.text}")

    # Parse routing info
    print("\n=== Routing ===")
    routing = root.find("Routing")

    # Static Routes
    static_routes = routing.find("StaticRoutes")
    print("Static Routes:")
    for route in static_routes.findall("Route"):
        print("  - Route:")
        for elem in route:
            print(f"    {elem.tag}: {elem.text}")

    # OSPF
    ospf = routing.find("OSPF")
    print("OSPF Configuration:")
    for elem in ospf:
        if elem.tag != "Networks":
            print(f"  {elem.tag}: {elem.text}")
        else:
            print("  Networks:")
            for network in elem.findall("Network"):
                print("    - Network:")
                for net_elem in network:
                    print(f"      {net_elem.tag}: {net_elem.text}")


# The main script 
if __name__ == "__main__":
    xml_file = "device.xml"
    parse_xml_config(xml_file)
