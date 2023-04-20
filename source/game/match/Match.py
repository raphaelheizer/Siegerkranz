"""
    A game match. Has no finite duration and should be persisted in database.
    It even could last years!
"""

import datetime
from typing import List, Optional

from source.game.actors.Country import Country
from source.game.actors.Player import Player


class Match:
    __winner = Optional[Player]

    def __init__(self, match_id, name: str, countries: List[Country], owner: Player,
                 finishing_time: Optional[datetime], is_open: bool):
        self.match_id = match_id
        self.__name = name
        self.__countries = countries
        self.__owner = owner
        self.__start_time = datetime.datetime.now()
        self.__finishing_time = finishing_time
        self.is_open = is_open  # Players can only join open matches

    def finish(self):
        self.__finishing_time = datetime.datetime.now()
        # Determine winner

    def set_winner(self, winner: Player):
        pass
