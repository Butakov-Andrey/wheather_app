import requests
from environs import Env

from .models import Wheather

env = Env()
env.read_env()


class GetWeather:
    API_ID = env("API_ID")
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, city):
        self.city = city

    def get_weather(self):
        params = {
            'q': self.city,
            'units': 'metric',
            'appid': self.API_ID
        }
        try:
            res = requests.get(self.BASE_URL, params=params).json()
            city_info = {
                'city': self.city,
                'temp': res['main']['temp'],
            }
        except KeyError:
            raise Exception('Bad request for wheather app/invalid city name')
        return city_info

    def insert_data(self):
        city_info = self.get_weather()
        wheather = Wheather(
            city=city_info['city'],
            temperature=city_info['temp']
        )
        wheather.save()
