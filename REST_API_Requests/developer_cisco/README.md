# DEVELOPER CISCO

## Access / Create the enviromnent
Access the Developer Cisco:

https://devnetsandbox.cisco.com/DevNet

Launch: Meraki Small Business and Enterprise

Create a personal account and give admin permissions

Create a API Key

## Returns the list of organization associated with the API key:

{{baseUrl}}/organizations

curl -L -H "X-Cisco-Meraki-API-Key: 5815f488a2d559fdc5a5911d08bd0189e97e261d" -H "Content-Type: application/json" -X GET "https://api.meraki.com/api/v1/organizations" -s | jq
  
- s : silent mode
jq : nice format and easy to read

id fied: it is the organization identifier

id organization: 803362

##########################################################################

## List all Networks associated with organizationId:

{{baseUrl}}/organizations/:organizationId/networks

curl -L -H "X-Cisco-Meraki-API-Key: 5815f488a2d559fdc5a5911d08bd0189e97e261d" -H "Content-Type: application/json" -X GET "https://api.meraki.com/api/v1/organizations/803362/networks" -s | jq

network id: 
L_711568741124547161

##########################################################################

## Obtain list of VLANs configured on specific network:

{{baseUrl}}/networks/:networkId/appliance/vlans

curl -L -H "X-Cisco-Meraki-API-Key: 5815f488a2d559fdc5a5911d08bd0189e97e261d" -H "Content-Type: application/json" -X GET "https://api.meraki.com/api/v1/networks/L_711568741124547161/appliance/vlans" -s | jq

##########################################################################

## Create vlan 10:

{{baseUrl}}/networks/:networkId/appliance/vlans

curl -L -H "X-Cisco-Meraki-API-Key: 5815f488a2d559fdc5a5911d08bd0189e97e261d" -H "Content-Type: application/json" -X POST --data '{"id": 10,"name": "Student VLAN", "subnet": "192.168.10.0/24", "applianceIp": "192.168.10.1" }' "https://api.meraki.com/api/v1/networks/L_711568741124547161/appliance/vlans" -s | jq


  
