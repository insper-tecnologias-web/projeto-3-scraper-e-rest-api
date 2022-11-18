import requests
import bs4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from abc import ABC, abstractmethod


# Public abstract class Scraper
class Scraper(ABC):

    def __init__(self, path):
        self.SCHEME: str = 'https://'
        self.HOST: str = 'boardgamegeek.com'

        self.PATH: str = ''.join(tuple(path))

        self.ua = UserAgent()
        self.headers = {'user-agent': self._ua.random}

    def generate_URL(self):
        url = ''.join(tuple(self.SCHEME, self.HOST, self.path))
        return url

    def soup_response(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    @abstractmethod
    def scrap(self):
        pass
