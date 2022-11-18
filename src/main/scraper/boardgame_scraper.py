from .scraper import Scraper
from .data import Data

import requests


class BoardgameScraper(Scraper):

    def __init__(self):
        super(path='/boardgame/')

        self.URL = self.generate_URL()

    # Private instance methods:
    def _get_game_duration(self):
        pass

    def _get_number_of_players(self):
        pass

    def _get_description(self):
        pass

    # Override abstract method from super class
    def scrap(self):
        pass
