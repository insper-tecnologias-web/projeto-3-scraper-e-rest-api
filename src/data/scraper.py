import bs4
from bs4 import BeautifulSoup

# Se precisar de aleatoriedade de user agent:
# pip install fake-useragent
# from fake_useragent import UserAgent


class Scraper:
    def __init__(self):
        self.SCHEME: str = 'https://'
        self.HOST: str = 'boardgamegeek.com'
        self.MAIN_PAGE_BASE_PATH: str = '/browse/boardgame/page/'
        self.BOARDGAME_PAGE_BASE_PATH: str = '/boardgame/'

        self.page: int = 1

    # Private instance methods
    def _generateURL(self, path):
        url = ''.join(tuple(self.SCHEME, self.HOST, path))
        return url

    def _getBoardgamePath(self, htmlTag_a):
        pass

    def _navigateToBoargamePage(self, boardgame_path):
        pass

    def _getGameDuration(self, boardgame_path):
        pass

    def _scrapMainPage(self):
        pass

    def _scrapBoardgamePage(self, boardgame_path):
        pass

    # Public instace method
    def run(self):
        pass
