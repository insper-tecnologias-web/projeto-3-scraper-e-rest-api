import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Scraper:

    def __init__(self):
        self.SCHEME: str = "https://"
        self.HOST: str = "boardgamegeek.com"
        self.path: str

        self.ua = UserAgent()
        self.headers = {"user-agent": self.ua.random}

    def generate_URL(self):
        url = "".join((self.SCHEME, self.HOST, self.path))
        return url

    def soup_response(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
