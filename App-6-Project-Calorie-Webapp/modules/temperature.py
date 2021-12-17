import requests
from selectorlib import Extractor


class Temperature:
    '''
    To get the temperature of the city from the web,
    precisely from from timeanddate.com
    '''
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
    base_url = 'https://www.timeanddate.com/weather'
    yaml_file = 'temperature.yaml'

    def __init__(self, city: str, country: str) -> None:
        self._city = city.replace(' ', '-').lower()
        self._country = country.lower()

    def url_builder(self):
        '''
        To build the url required to get to the webpage
        '''
        url = f'{self.base_url}/{self._country}/{self._city}'
        return url

    def get_temperature(self):
        '''
        Scrpes the data from the url of the url_builder
        '''
        responce = requests.get(url=self.url_builder, headers=self.headers_text)
        text_responce = responce.text
        extractor = Extractor.from_yaml_file(self.yaml_file)
        raw_result = extractor.extract(text_responce)
        return raw_result

    def get(self):
        '''
        Replace unnecessary content and returns the integer
        '''
        scrapped_content = self.get_temperature()
        return int(scrapped_content['temp'].replace('°C', '').strip())


if __name__ == '__main__':
    temp = Temperature('New Delhi', 'India')
    print(temp.get())
