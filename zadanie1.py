import requests


def check_url(url: str) -> bool:
    response = requests.get(url)
    return (response.status_code > 199) and (response.status_code < 300)



print(check_url("http://wmii.uwm.edu.pl/kadra"))
