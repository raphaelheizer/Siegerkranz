"""
    Representation of a server's lobby and all matches available at a time. It should be unique in a server
"""

from typing import List

from source.game.actors.Player import Player
from source.game.match.Match import Match
from source.object_scopes.Singleton import Singleton


class Lobby(metaclass=Singleton):

    def __init__(self, room_id, owner: Player, matches: List[Match]):
        self.room_id = room_id
        self.__owner = owner
        self.matches = matches
