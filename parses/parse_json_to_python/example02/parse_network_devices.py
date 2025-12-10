import json

def parse_network_devices(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        if 'devices' not in data:
            raise KeyError("Missing 'devices' key in JSON.")

        devices = data['devices']
        if not isinstance(devices, list):
            raise ValueError("'devices' should be a list.")

        return devices

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except (KeyError, ValueError) as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []


if __name__ == "__main__":
    devices = parse_network_devices("network_devices.json")

    if devices:
        print("\nParsed Network Devices:\n")
        for device in devices:
            print(f"Hostname: {device['hostname']}")
            print(f"Type: {device['device_type']}")
            print(f"IP: {device['ip_address']}")
            print(f"Location: {device['location']}")
            print("Interfaces:")
            for interface in device.get('interfaces', []):
                print(f" - {interface['name']} ({interface['status']}) -> IP: {interface['ip']}")

            print("-" * 40)

