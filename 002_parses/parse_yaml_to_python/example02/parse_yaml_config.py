import yaml

def parse_yaml_config(file_path):
    """Parses YAML data from a given file path and returns the Python dictionary."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def display_device_info(devices):
    """Displays parsed device information in a readable format."""
    for device in devices.get('devices', []):
        print(f"\nDevice Name: {device['name']}")
        print(f"  Type: {device['type']}")
        print(f"  IP Address: {device['ip']}")
        print(f"  Location: {device['location']}")
        print("  Interfaces:")
        for intf in device['interfaces']:
            intf_info = "    " + ", ".join([f"{k.capitalize()}: {v}" for k, v in intf.items()])
            print(intf_info)

if __name__ == "__main__":
    yaml_file = "devices.yaml"
    parsed_data = parse_yaml_config(yaml_file)
    display_device_info(parsed_data)

