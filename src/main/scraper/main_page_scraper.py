import json
from pathlib import Path

from bs4 import BeautifulSoup
from scraper import Scraper

from data import MainData


class MainPageScraper(Scraper):

    def __init__(self):
        super().__init__()
        self.page = 1
        self.path = "/browse/boardgame/page/"
        self.href_list = []
        self.scraped_data = []
        self.URL = self.generate_URL()
        self.data = MainData()
        self.json_dir = Path(__file__).parent.cwd() / "src" / "data" / "data.json"

    def __next_page(self):
        self.page += 1
        self.URL = self.generate_URL()

    def __get_rows(self):
        table = self.__get_table()
        rows = table.find_all("tr", {"id": "row_"})
        return rows

    def __get_table(self):
        soup = self.__soup_response()
        table = soup.find(
            "table", {"id": "collectionitems", "class": "collection_table"}
        )
        return table

    def __handle_table_row_data(self, row):
        self.__get_hrefs(row)
        self.__attribute_bgg_rank_to_data(row)
        self.__attribute_boardgame_name_to_data(row)
        self.__attribute_boardgame_year_to_data(row)
        self.__attribute_three_rating_types_data_to_data(row)
        # self.__attribute_amazon_price_to_data(row)

    def __get_hrefs(self, row):
        href = row.find("a", {"class": "primary"}, href=True)["href"]
        self.href_list.append(href)

    def __attribute_bgg_rank_to_data(self, row):
        bgg_rank = row.find("td", {"class": "collection_rank"}).text
        bgg_rank = int(bgg_rank)
        self.data.RANK = bgg_rank

    def __attribute_boardgame_name_to_data(self, row):
        boardgame_name = row.find("a", {"class": "primary"}).text
        self.data.NAME = boardgame_name

    def __attribute_boardgame_year_to_data(self, row):
        try:
            boardgame_year = row.find("span", {"class": "smallerfont dull"}).text[1:-1]
            boardgame_year = int(boardgame_year)
            self.data.YEAR = boardgame_year
        except Exception:
            pass

    def __attribute_three_rating_types_data_to_data(self, row):
        three_rating_data = row.find_all("td", {"class": "collection_bggrating"})
        self.data.BGG_RATING = float(three_rating_data[0].text)
        self.data.AVG_RATING = float(three_rating_data[1].text)
        self.data.NUM_VOTERS = int(three_rating_data[2].text)

    # def __attribute_amazon_price_to_data(self, row):
    #     try:
    #         amazon_price = row.find('td', {'class': 'collection_shop'}).find(
    #             'span', {'class': 'positive'}).text[1:]
    #         amazon_price = (amazon_price)
    #         # self.data.AMAZON_PRICE = amazon_price
    #     except:
    #         pass

    def __soup_response(self) -> BeautifulSoup:
        url_with_page = "".join((self.URL, str(self.page)))
        soup = self.soup_response(url_with_page)
        return soup

    def __handle_rows(self):
        rows = self.__get_rows()
        for row in rows:
            self.__handle_table_row_data(row)
            data_dict = self.data.make_dict()
            self.scraped_data.append(data_dict)

    def write_on_json(self):
        self.scraped_data = json.dumps(self.scraped_data, indent=4)
        with open(self.json_dir, "w") as json_file:
            json_file.write(self.scraped_data)

    def scrap(self):
        while True:
            try:
                print(self.page)
                self.__handle_rows()
                self.__next_page()
            except Exception:
                break


if __name__ == "__main__":
    scraper = MainPageScraper()
    scraper.scrap()
    scraper.write_on_json()
