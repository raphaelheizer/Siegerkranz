"""
    Representation of a server's lobby and all matches available at a time. It should be unique in a server
"""

from typing import List

from source.game.actors.Player import Player
from source.game.chat.Chat import Chat
from source.game.match.Match import Match
from source.object_scopes.Singleton import Singleton


class Lobby(metaclass=Singleton):

    def __init__(self, matches: List[Match], joined_players: List[Player], chat: Chat):
        self.matches = matches
        self.__joined_players = joined_players
        self.chat = chat
