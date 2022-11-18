import bs4
from bs4 import BeautifulSoup

# Se precisar de aleatoriedade de user agent:
# pip install fake-useragent
# from fake_useragent import UserAgent

class Scraper:
    def __init__(self):
        self.SCHEME = 'https://'
        self.HOST:str = 'boardgamegeek.com'
        self.MAIN_PAGE_BASE_PATH:str = '/browse/boardgame/page/'
        self.BOARDGAME_PAGE_BASE_PATH:str = '/boardgame/'

        self.page:int = 1
        pass

    def __generateURL(self, path):
        return self.SCHEME + self.HOST + path

    def getBoardgameURI(self, htmlTag_a):
        pass

    def navigateToBoargamePage(self, boardgame_path):
        pass

    def getGameDuration(self, boardgame_path):
        pass

    def scrap(self):
        pass