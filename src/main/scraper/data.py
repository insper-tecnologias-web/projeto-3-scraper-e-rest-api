class Data:

    def __init__(self):
        self.BGG_RANK = ''
        self.BOARDGAME_NAME = ''
        self.BOARDGAME_YEAR = ''
        self.BGG_RATING = ''
        self.AVG_RATING = ''
        self.NUM_VOTERS = ''
        self.AMAZON_PRICE = ''

    def make_dict(self) -> dict:
        data_dict = {
            'bgg_rank': self.BGG_RANK,
            'boardgame_name': self.BOARDGAME_NAME,
            'boardgame_year': self.BOARDGAME_YEAR,
            'bgg_rating': self.BGG_RATING,
            'avg_rating': self.AVG_RATING,
            'num_voters': self.NUM_VOTERS,
            'amazon_price': self.AMAZON_PRICE
        }
        return data_dict
