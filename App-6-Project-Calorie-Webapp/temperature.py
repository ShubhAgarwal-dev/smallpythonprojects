import requests
from selectorlib import Extractor


class Temperature:
    '''
    To get the temperature of the city from the web,
    preciselt from from timaanddate.com
    '''

    def __init__(self, city, country) -> None:
        self._city = city
        self._country = country

    def get_temperature(self):
        headers_text = {
            'pragma':
                'no-cache',
            'cache-control':
                'no-cache',
            'dnt':
                '1',
            'upgrade-insecure-requests':
                '1',
            'user-agent':
                'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept':
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language':
                'en-GB,en-US;q=0.9,en;q=0.8',
        }  # Just so that website can beleave that request is from the web
        responce = requests.get(
            url=f'https://www.timeanddate.com/weather/{self._country}/{self._city}',
            headers=headers_text)
        text_responce = responce.text()
