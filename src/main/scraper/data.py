class MainData:

    def __init__(self):
        self.RANK: int = None
        self.NAME: str = None
        self.YEAR: int = None
        self.BGG_RATING: float = None
        self.AVG_RATING: float = None
        self.NUM_VOTERS: int = None
        self.AMAZON_PRICE: float = None

    def make_dict(self) -> dict:
        data_dict = {
            'rank': self.RANK,
            'name': self.NAME,
            'year': self.YEAR,
            'bgg_rating': self.BGG_RATING,
            'avg_rating': self.AVG_RATING,
            'num_voters': self.NUM_VOTERS,
            'amazon_price': self.AMAZON_PRICE
        }
        return data_dict


class BoardgameData:

    def __init__(self):
        self.NUMBER_OF_PLAYERS: str
        self.GAME_DURATION: str
        self.DESCRIPTION: str

    def make_dict(self) -> dict:
        data_dict = {
            'number_of_players': self.NUMBER_OF_PLAYERS,
            'game_duration': self.GAME_DURATION,
            'description': self.DESCRIPTION
        }
        return data_dict
