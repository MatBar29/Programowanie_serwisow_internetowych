import requests

url = 'http://wmii.uwm.edu.pl/'
response = requests.get(url)

print('Kod odpowiedzi ', response.status_code)
print('Tresc odpowiedzi ', response.content)
print('Naglowki ', response.headers)