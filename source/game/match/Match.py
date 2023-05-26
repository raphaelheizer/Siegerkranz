"""
    A game match. Has no finite duration and should be persisted in database.
    It even could last years!
"""

import datetime
from typing import List, Optional

from source.game.actors.Country import Country
from source.game.actors.Player import Player
from source.game.chat.Chat import Chat


class Match:
    __winner = Optional[Player]

    def __init__(self, match_id, name: str, countries: List[Country], owner: Player,
                 chat: Chat, finishing_time: Optional[datetime], players: List[Player], is_open: bool = True):
        self.match_id = match_id
        self.__name = name
        self.__countries = countries
        self.__owner = owner
        self.__start_time = datetime.datetime.now()
        self.__finishing_time = finishing_time
        self.players = players
        self.is_open = is_open  # Players can only join open matches
        self.chat = chat
        self.chat.connected_players = players

    def finish(self):
        self.__finishing_time = datetime.datetime.now()
        # Determine winner

    def set_winner(self, winner: Player):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'match_id={self.match_id}|name={self.__name}|countries={self.__countries.__str__()}|' \
               f'owner={self.__owner.name}|player_count={len(self.players)}|match_open={self.is_open}'
