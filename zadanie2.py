import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.meteoprog.pl/pl/weather/Olsztyn/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temp_now = soup.find('span', class_='today-temperature')

hourly_temp_section = soup.find('ul', class_='today-hourly-weather')

hours = []
temperatures = []

for hour_block in hourly_temp_section.find_all('li'):
    hour = hour_block.find('span', class_='today-hourly-weather__name').text
    temperature = hour_block.find('span', class_='today-hourly-weather__temp').text
    temperatures.append(int(temperature.replace("°", "")))
    hours.append(hour)

plt.figure(figsize=(10, 5))
plt.plot(hours, temperatures, marker='o')
plt.title(f'Temperatura w Olsztynie na najbliższe godziny')
plt.xlabel('Godzina')
plt.ylabel('Temperatura (°C)')
plt.grid(True)

plt.show()
