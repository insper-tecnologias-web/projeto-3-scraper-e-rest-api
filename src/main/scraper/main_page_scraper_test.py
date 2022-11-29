from main_page_scraper import MainPageScraper

import unittest


class TestBeforeScrape(unittest.TestCase):
    def setUp(self):
        self.Scraper = MainPageScraper()

    def test_url(self):
        url_from_object = self.Scraper.URL
        url_expected = 'https://boardgamegeek.com/browse/boardgame/page/1'
        self.assertEqual(url_from_object, url_expected,
                         'A URL gerada está incorreta')

    def test_RANK_data_before_scrape(self):
        RANK_from_object = self.Scraper.data.RANK
        RANK_expected = None
        self.assertEqual(RANK_from_object, RANK_expected,
                         'RANK não está nulo')

    def test_NAME_data_before_scrape(self):
        NAME_from_object = self.Scraper.data.NAME
        NAME_expected = None
        self.assertEqual(NAME_from_object, NAME_expected,
                         'NAME não está nulo')

    def test_YEAR_data_before_scrape(self):
        YEAR_from_object = self.Scraper.data.YEAR
        YEAR_expected = None
        self.assertEqual(YEAR_from_object, YEAR_expected,
                         'YEAR não está nulo')

    def test_BGG_RATING_data_before_scrape(self):
        BGG_RATING_from_object = self.Scraper.data.BGG_RATING
        BGG_RATING_expected = None
        self.assertEqual(BGG_RATING_from_object,
                         BGG_RATING_expected, 'BGG_RATING não está nulo')

    def test_AVG_RATING_data_before_scrape(self):
        AVG_RATING_from_object = self.Scraper.data.AVG_RATING
        AVG_RATING_expected = None
        self.assertEqual(AVG_RATING_from_object,
                         AVG_RATING_expected, 'AVG_RATING não está nulo')

    def test_NUM_VOTERS_data_before_scrape(self):
        NUM_VOTERS_from_object = self.Scraper.data.NUM_VOTERS
        NUM_VOTERS_expected = None
        self.assertEqual(NUM_VOTERS_from_object,
                         NUM_VOTERS_expected, 'NUM_VOTERS não está nulo')

    # def test_AMAZON_PRICE_data_before_scrape(self):
    #     AMAZON_PRICE_from_object = self.Scraper.data.AMAZON_PRICE
    #     AMAZON_PRICE_expected = None
    #     self.assertEqual(AMAZON_PRICE_from_object,
    #                      AMAZON_PRICE_expected, 'AMAZON_PRICE não está nulo')


# class Test(unittest.TestCase):
#     def setUp(self):
#         # ESSE CÓDIGO ABAIXO NÃO PODE SER USADO COMO TESTE, DADO QUE
#         # OS DADOS VARIAM COM O TEMPO, QUAL FORMA MELHOR DE TESTAR??
#         self.Scraper = MainPageScraper()
#         self.Scraper.scrap()
#         self.scraped_data = self.Scraper.scraped_data[0]

#         # Solução ruim: alterar os dados conforme visto no site
#         # https://boardgamegeek.com/browse/boardgame/page/1
#         self.RANK_expected = 1
#         self.NAME_expected = 'Gloomhaven'
#         self.YEAR_expected = 2017
#         self.BGG_RATING_expected = 8.452
#         self.AVG_RATING_expected = 8.68
#         self.NUM_VOTERS_expected = 53344
#         self.AMAZON_PRICE_expected = 165.00
        

#     def test_RANK_data_after_scrape(self):
#         RANK_from_object = self.scraped_data['rank']
#         self.assertEqual(RANK_from_object, self.RANK_expected,
#                          'RANK raspado está diferente')

#     def test_NAME_data_after_scrape(self):
#         NAME_from_object = self.scraped_data['name']
#         self.assertEqual(NAME_from_object, self.NAME_expected,
#                          'NAME raspado está diferente')

#     def test_YEAR_data_after_scrape(self):
#         YEAR_from_object = self.scraped_data['year']
#         self.assertEqual(YEAR_from_object, self.YEAR_expected,
#                          'ANO raspado está diferente')

#     def test_BGG_RATING_data_after_scrape(self):
#         BGG_RATING_from_object = self.scraped_data['bgg_rating']
#         self.assertEqual(BGG_RATING_from_object,
#                          self.BGG_RATING_expected, 'BGG_RATING raspado está diferente')

#     def test_AVG_RATING_data_after_scrape(self):
#         AVG_RATING_from_object = self.scraped_data['avg_rating']
#         self.assertEqual(AVG_RATING_from_object,
#                          self.AVG_RATING_expected, 'AVG_RATING raspado está diferente')

#     def test_NUM_VOTERS_data_after_scrape(self):
#         NUM_VOTERS_from_object = self.scraped_data['num_voters']
#         self.assertEqual(NUM_VOTERS_from_object,
#                          self.NUM_VOTERS_expected, 'NUM_VOTERS raspado está diferente')

#     def test_AMAZON_PRICE_data_after_scrape(self):
#         AMAZON_PRICE_from_object = self.scraped_data['amazon_price']
#         self.assertEqual(AMAZON_PRICE_from_object,
#                          self.AMAZON_PRICE_expected, 'AMAZON_PRICE raspado está diferente')


if __name__ == '__main__':
    unittest.main()
