import requests
from pprint import pprint
import secrets

url = f"https://api.meraki.com/api/v1/networks/{secrets.NETWORK_ID}/appliance/vlans"

headers = {
    "X-Cisco-Meraki-API-Key": secrets.API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    pprint(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")