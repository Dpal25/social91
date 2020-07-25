import requests
import sys
import json

f = open(sys.argv[1])
data = json.load(f)
total_price = 0
component_prices = []

date = data['date']

request_data = {
    'date' : date,
}

url = 'http://localhost:8000/getprice/'
response = requests.post(url, data=request_data)

if response.status_code != 200:
    print('Failed to receive data')

for component in data['components']:
    component_price = 0
    for part in data['components'][component]:
        component_price += response.json()['Pricing'][part]
    total_price += component_price
    component_prices.append(component_price)
    print('Price of ' + component + ' ' + str(component_price))

print('Total price of cycle = ' + str(total_price))


