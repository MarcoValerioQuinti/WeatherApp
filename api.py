from pkgutil import get_data
from turtle import title
from webbrowser import get
import requests, json

class Api:

    def __init__(self) -> None:
        pass

    def jprint(obj):
        # format json
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def get_woeid(city):
        get_woeid = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')
        get_woeid = get_woeid.json()[0]

        woeid = get_woeid['woeid']
        return woeid

    def get_data(self, city):
        get_data = requests.get(f'https://www.metaweather.com/api/location/{Api.get_woeid(city)}/')
        data = get_data.json()
        return data
