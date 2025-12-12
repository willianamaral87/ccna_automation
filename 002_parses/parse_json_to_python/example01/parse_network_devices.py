import json
from typing import List, Dict

def parse_network_devices(json_file: str) -> List[Dict]:
    """
    Parses the given JSON file and returns a list of network devices.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        devices = data.get("devices", [])
        if not devices:
            print("⚠️ No devices found in the JSON file.")
        return devices

    except FileNotFoundError:
        print(f"❌ The file {json_file} does not exist.")
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
    return []

# Example usage
if __name__ == "__main__":
    devices = parse_network_devices("network_devices.json")
    for device in devices:
        print(f"\n�� Hostname: {device['hostname']}")
        print(f"   📍 IP Address: {device['ip_address']}")
        print(f"   🧰 Type: {device['device_type']}")
        print(f"   📦 Location: {device['location']}")
        print(f"   🔌 Interfaces:")
        for intf in device["interfaces"]:
            print(f"     - {intf['name']} | IP: {intf['ip']} | Status: {intf['status']}")
