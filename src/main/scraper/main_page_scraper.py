from .scraper import Scraper
from .data import Data

import requests
import bs4
from bs4 import BeautifulSoup


class MainPageScraper(Scraper):

    def __init__(self):
        super(path='/browse/boardgame/page/')

        self.page = 1
        self.URL = self.generate_URL()

        self.data = Data()

    # ===== Private instance methods
    def _find_table(self) -> bs4.element.tag | bs4.element.NavigableString:
        soup = self._soup_response()
        table = soup.find('table', class_='collection_table').find('tbody')
        return table

    # Find rows of the table
    def _find_rows(self) -> list:
        table = self._find_table()
        rows = table.find_all('tr', id='row')
        return rows

    # ----- Table row data
    def _bgg_rank(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:
        bgg_rank = row.find('td', class_='collection_rank').text
        self.data.BGG_RANK = bgg_rank
        return bgg_rank

    def _boardgame_name(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:
        boardgame_name = row.find('a', class_='primary').text
        self.data.BOARDGAME_NAME = boardgame_name
        return boardgame_name

    def _boardgame_year(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:
        boardgame_year = row.find('span', class_='smallerfont dull').text
        self.data.BOARDGAME_YEAR = boardgame_year
        return boardgame_year

    def _bgg_rating(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:

        pass

    def _avg_rating(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:

        pass

    def _num_voters(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:

        pass

    def _amazon_price(self, row: bs4.element.tag | bs4.element.NavigableString) -> bs4.element.tag | bs4.element.NavigableString:

        pass
    # ----- End table row data

    def _soup_response(self) -> BeautifulSoup:
        url_with_page = ''.join(tuple(self.URL, self.page))
        response = requests.get(url_with_page, headers=self.headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    # Override abstract method from super class
    def scrap(self) -> None:
        scraped_data: list

        rows = self._find_rows()
        for row in rows:
            data_dict = self.data.make_dict()

            scraped_data.append(data_dict)
