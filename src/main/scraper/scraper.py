import requests
import bs4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from abc import ABC, abstractmethod


# Abstract class Scraper
class Scraper(ABC):

    def __init__(self, path):
        self.SCHEME: str = 'https://'
        self.HOST: str = 'boardgamegeek.com'

        self.PATH: str = ''.join(tuple(path))

        self.ua = UserAgent()
        self.headers = {'user-agent': self._ua.random}

    def _navigate_to_boardgame_page(self, boardgame_path):
        pass

    def generate_URL(self):
        url = ''.join(tuple(self.SCHEME, self.HOST, self.path))
        return url

    def get_tag_a(self):
        pass

    def get_href_from_a(self, htmlTag_a):
        pass

    @abstractmethod
    def scrap(self):
        pass
