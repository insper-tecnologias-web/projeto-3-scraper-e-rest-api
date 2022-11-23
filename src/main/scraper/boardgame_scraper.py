from .scraper import Scraper
from .data import BoardgameData

from bs4 import BeautifulSoup


# TODO: instanciar o super().PATH com base no href
# Enquanto isso não for feito, não poderá ser testado
class BoardgameScraper(Scraper):

    def __init__(self):
        super().__init__()
        self.href = '????????????????????????'
        self.URL = self.generate_URL()
        self.li_tags = []
        self.data = BoardgameData()

    def __handle_boardgame_data(self):
        self.__attribute_number_of_players_to_data()
        self.__attribute_game_duration_to_data()
        self.__attribute_description_to_data()

    def __attribute_number_of_players_to_data(self):
        players_span_range = self.__get_players_span_range()
        try:
            players_span_range = players_span_range.text.split('-')
            players_range = list(map(int, players_span_range))
        except:
            players_range = int(players_span_range)
        self.data.NUMBER_OF_PLAYERS = players_range

    def __get_players_span_range(self):
        li_tag = self.li_tags()[0]
        players_div = li_tag.find('div', class_='gameplay-item-primary')
        players_span_range = players_div.find(
            'span', class_='ng-scope ng-isolate-scope')
        return players_span_range

    def __attribute_game_duration_to_data(self):
        game_duration_span_range = self.__get_game_duration_span_range()
        try:
            game_duration_span_range = game_duration_span_range.text.split('-')
            game_duration_range = list(map(int, game_duration_span_range))
        except:
            game_duration_range = int(game_duration_span_range)
        self.data.GAME_DURATION = game_duration_range

    def __get_game_duration_span_range(self):
        li_tag = self.li_tags()[1]
        game_duration_div = li_tag.find('div', class_='gameplay-item-primary')
        game_duration_span_range = game_duration_div.find(
            'span', class_='ng-isolate-scope')
        return game_duration_span_range

    def __attribute_description_to_data(self):
        soup = self.__soup_response()
        description_article = soup.find(
            'article', class_='game-description-body ng-scope')
        paragraphs = description_article.find_all('p')
        description = '\n'.join(paragraphs)
        self.data.DESCRIPTION = description

    def __soup_response(self) -> BeautifulSoup:
        url_with_href = ''.join(tuple(self.URL, self.href))
        soup = self.soup_response(url_with_href)
        return soup

    def __get_li_tags(self):
        game_stats_div = self.__get_game_stats_div()
        self.li_tags = game_stats_div.find_all('li', class_='gameplay-item')

    def __get_game_stats_div(self):
        soup = self.__soup_response()
        game_stats_div = soup.find('div', class_='panel panel-bottom ng-scope')
        return game_stats_div


    def scrap(self) -> dict:
        self.__get_li_tags()
        self.__handle_boardgame_data()
        data_dict = self.data.make_dict()

        return data_dict
