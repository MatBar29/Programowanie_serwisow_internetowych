import requests
import json

url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
response = requests.get(url)

response.content

response.content.decode('utf-8')

content = response.content.decode('utf-8')
parsed_content = json.loads(content)

print(type(response.content), type(content), type(parsed_content))

for station in parsed_content:
    print(
        f'ID: {station["id"]}, nazwa: {station["stationName"]}, miasto: {station["city"]["name"]}, lokalizacja: {station["addressStreet"]}')

print("------------------------------------------")

station_id = 877
url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
response = requests.get(url)

if response.status_code != 200:
  exit()

stations = json.loads(response.content.decode('utf-8'))

print(stations)

print("------------------------------------------")

import requests
import json

sensor_id = 5766
url = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensor_id}'
response = requests.get(url)

if response.status_code != 200:
  assert False

data = json.loads(response.content.decode('utf-8'))
value = data['values'][0]

print(f'Czas: {value["date"]}, wartosc odczytu: {value["value"]}')