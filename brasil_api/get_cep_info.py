import requests

#cep = input("Type the CEP:")

cep = '13013000'

url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

response = requests.get(url)

print(f"Response code: {response.status_code}")
print(f"Response Text: {response.text}")
print(f"Response Reason: {response.reason}")
print(f"Response URL: {response.url}")
print(f"Response OK (True if status < 400)): {response.ok}")

print('-'*152)

data = response.json()

print(f"Dictionary format: {data}")
print(f"neighborhood : {data['neighborhood']}")
print(f"City         : {data['city']}")
print(f"State        : {data['state']}")
print(f"Street       : {data['street']}")
print(f"CEP          : {data['cep']}")
