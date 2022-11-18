from .scraper import Scraper
from .data import Data

import re
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
    def _find_table(self):
        soup = self._soup_response()
        table = soup.find('table', class_='collection_table').find('tbody')
        return table

    # Find rows of the table
    def _find_rows(self) -> list:
        table = self._find_table()
        rows = table.find_all('tr', id='row')
        return rows

    # ----- Table row data
    def _bgg_rank(self, row):
        bgg_rank = row.find('td', class_='collection_rank').text
        self.data.BGG_RANK = bgg_rank

    def _boardgame_name(self, row):
        boardgame_name = row.find('a', class_='primary').text
        self.data.BOARDGAME_NAME = boardgame_name

    def _boardgame_year(self, row):
        boardgame_year = row.find('span', class_='smallerfont dull').text[1:-1]
        self.data.BOARDGAME_YEAR = boardgame_year

    def _three_rating_data(self, row):
        three_rating_data = row.find_all('td', class_='collection_bggrating')
        self.data.BGG_RATING = three_rating_data[0].text
        self.data.AVG_RATING = three_rating_data[1].text
        self.data.NUM_VOTERS = three_rating_data[2].text

    def _amazon_price(self, row):
        amazon_price = row.find('a', class_='ulprice').find(
            'span', class_='positive').text[1:]
        self.data.AMAZON_PRICE = amazon_price
    # ----- End table row data

    def _handle_table_row_data(self, row):
        self._bgg_rank(row)
        self._boardgame_name(row)
        self._boardgame_year(row)
        self._three_rating_data(row)
        self._amazon_price(row)

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
            self._handle_table_row_data(row)
            data_dict = self.data.make_dict()

            scraped_data.append(data_dict)
