import requests
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.meteoprog.pl/pl/weather/Olsztyn/'
response = requests.get(url)

soup = BeautifulSoup(response.content, features="html.parser")
table = soup.find('ul', class_='today-hourly-weather hide-scroll').find('li')

print(table)