import datetime
from typing import List, Optional

from source.game.actors.Country import Country
from source.game.actors.Player import Player


class Match:
    __winner = Optional[Player]

    def __init__(self, countries: List[Country], finishing_time: Optional[datetime]):
        self.__countries = countries
        self.__start_time = datetime.datetime.now()
        self.__finishing_time = finishing_time

    def finish(self):
        self.__finishing_time = datetime.datetime.now()
        # Determine winner
