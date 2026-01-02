import requests
from pprint import pprint
import secrets

VLAN_ID = 40
url = f"https://api.meraki.com/api/v1/networks/{secrets.NETWORK_ID}/appliance/vlans/{VLAN_ID}"

headers = {
    "X-Cisco-Meraki-API-Key": secrets.API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "name": "Lab VLAN 40 Patched"
}

response = requests.put(url, headers=headers, json=payload)

if response.status_code == 200:
    pprint(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")