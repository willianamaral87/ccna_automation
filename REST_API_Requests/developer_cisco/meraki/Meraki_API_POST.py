import requests
from pprint import pprint
import secrets

url = f"https://api.meraki.com/api/v1/networks/{secrets.NETWORK_ID}/appliance/vlans"

headers = {
    "X-Cisco-Meraki-API-Key": secrets.API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "id": 40,
    "name": "Lab VLAN 40",
    "subnet": "192.168.40.0/24",
    "applianceIp": "192.168.40.1"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code in [200, 201]:
    pprint(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
