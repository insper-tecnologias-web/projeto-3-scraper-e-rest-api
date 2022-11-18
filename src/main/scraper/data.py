from abc import ABC, abstractmethod


class Data(ABC):
    @abstractmethod
    def make_dict(self) -> dict:
        pass


class MainData(Data):

    def __init__(self):
        self.BGG_RANK: str
        self.BOARDGAME_NAME: str
        self.BOARDGAME_YEAR: str
        self.BGG_RATING: str
        self.AVG_RATING: str
        self.NUM_VOTERS: str
        self.AMAZON_PRICE: str

    # Override abstract method from superclass
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


class BoardgameData(Data):

    def __init__(self):
        self.NUMBER_OF_PLAYERS: str
        self.GAME_DURATION: str
        self.DESCRIPTION: str

    # Override abstract method from superclass
    def make_dict(self) -> dict:
        data_dict = {
            'number_of_players': self.NUMBER_OF_PLAYERS,
            'game_duration': self.GAME_DURATION,
            'description': self.DESCRIPTION
        }
        return data_dict
