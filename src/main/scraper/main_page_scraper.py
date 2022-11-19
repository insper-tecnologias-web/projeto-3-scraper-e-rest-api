from .scraper import Scraper
from .data import MainData

import requests
import bs4
from bs4 import BeautifulSoup


class MainPageScraper(Scraper):

    def __init__(self):
        super(path='/browse/boardgame/page/')
        self.href_list: list

        self.page = 1
        self.URL = self.generate_URL()

        self.data = MainData()

    # ===== Private instance methods
    # def _next_page(self):
    #     self.page += 1
    #     self.URL = self.generate_URL()

    # def _previous_page(self):
    #     self.page -= 1
    #     self.URL = self.generate_URL()

    def _find_hrefs(self):
        rows = self._find_rows()
        for row in rows:
            href = row.find('a', class_='primary', href=True)['href']
            self.hrefs_list.append(href)

    def _find_table(self):
        soup = self._soup_response()
        table = soup.find('table', class_='collection_table').find('tbody')
        return table

    def _find_rows(self) -> list:
        table = self._find_table()
        rows = table.find_all('tr', id='row')
        return rows

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

    def _handle_table_row_data(self, row):
        self._bgg_rank(row)
        self._boardgame_name(row)
        self._boardgame_year(row)
        self._three_rating_data(row)
        self._amazon_price(row)

    def _soup_response(self) -> BeautifulSoup:
        url_with_page = ''.join(tuple(self.URL, self.page))
        soup = self.soup_response(url_with_page)
        return soup

    # Override abstract method from super class
    def scrap(self) -> list:
        scraped_data: list

        rows = self._find_rows()
        for row in rows:
            self._handle_table_row_data(row)
            data_dict = self.data.make_dict()

            scraped_data.append(data_dict)
        return scraped_data
