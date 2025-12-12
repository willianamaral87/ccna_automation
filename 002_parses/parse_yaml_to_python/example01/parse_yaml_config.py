import yaml

def parse_yaml_config(file_path):
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)

    device_config = config["NetworkDeviceConfig"]

    # Device Info
    print("=== Device Information ===")
    for key, value in device_config["Device"].items():
        print(f"{key}: {value}")

    # Interfaces
    print("\n=== Interfaces ===")
    for interface in device_config["Interfaces"]:
        print("--- Interface ---")
        for key, value in interface.items():
            print(f"{key}: {value}")

    # Static Routes
    print("\n=== Static Routes ===")
    for route in device_config["Routing"]["StaticRoutes"]:
        print("  - Route:")
        for key, value in route.items():
            print(f"    {key}: {value}")

    # OSPF
    print("\n=== OSPF Configuration ===")
    ospf = device_config["Routing"]["OSPF"]
    print(f"  ProcessID: {ospf['ProcessID']}")
    print(f"  RouterID: {ospf['RouterID']}")
    print("  Networks:")
    for network in ospf["Networks"]:
        print("    - Network:")
        for key, value in network.items():
            print(f"      {key}: {value}")

if __name__ == "__main__":
    yaml_file = "devices.yaml"
    parse_yaml_config(yaml_file)
