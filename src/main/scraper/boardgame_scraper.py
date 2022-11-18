from .scraper import Scraper
from .data import BoardgameData

import requests
import bs4
from bs4 import BeautifulSoup


class BoardgameScraper(Scraper):

    def __init__(self):
        super(path='/boardgame/')

        self.href: str

        self.URL = self.generate_URL()

        self.data = BoardgameData()

    # Private instance methods:

    def _find_game_stats_div(self):
        soup = self._soup_response()
        game_stats_div = soup.find('div', class_='panel panel-bottom ng-scope')
        return game_stats_div

    def _find_li_tags(self) -> list:
        game_stats_div = self._find_game_stats_div()
        li_tags = game_stats_div.find_all('li', class_='gameplay-item')
        return li_tags

    # ----- Data
    def _number_of_players(self) -> tuple:
        li_tag = self._find_li_tags()[0]
        players_div = li_tag.find('div', class_='gameplay-item-primary')
        players_span_range = players_div.find(
            'span', class_='ng-scope ng-isolate-scope')
        try:
            players_span_range = players_span_range.text.split('-')
            players_range = list(map(int, players_span_range))
        except:
            players_range = int(players_span_range)
        self.data.NUMBER_OF_PLAYERS = players_range

    def _game_duration(self, li_tag) -> tuple:
        li_tag = self._find_li_tags()[1]
        game_duration_div = li_tag.find('div', class_='gameplay-item-primary')
        game_duration_span_range = game_duration_div.find(
            'span', class_='ng-isolate-scope')
        try:
            game_duration_span_range = game_duration_span_range.text.split('-')
            game_duration_range = list(map(int, game_duration_span_range))
        except:
            game_duration_range = int(game_duration_span_range)
        self.data.GAME_DURATION = game_duration_range
        
    def _description(self):
        soup = self._soup_response()
        description_article = soup.find('article', class_='game-description-body ng-scope')
        paragraphs = description_article.find_all('p')
        description = '\n'.join(paragraphs)
        self.data.DESCRIPTION = description
    # -----

    def _handle_boardgame_data(self):
        self._number_of_players()
        self._game_duration()
        self._description()

    def _soup_response(self):
        soup = self.soup_response(self.URL)
        return soup

    # Override abstract method from super class
    def scrap(self) -> dict:
        self._handle_boardgame_data()
        data_dict = self.data.make_dict()

        return data_dict