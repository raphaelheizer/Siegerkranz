"""
    Manages the state of all the game matches. Must be unique
"""
import uuid
from typing import List

from source.game.actors.Country import Country
from source.game.actors.Player import Player
from source.game.lobby.Lobby import Lobby
from source.game.match.Match import Match
from source.object_scopes.Singleton import Singleton


class GameLobbyManager(metaclass=Singleton):
    def __init__(self):
        # Load if there is any running matches in database
        self.__lobby = Lobby([], [])

    def create_match(self, owner: Player, name: str):
        # Generate random ID for the match
        match_uid = uuid.uuid4()
        new_match = Match(match_uid, name, self.__populate_default_countries(), owner, None, True)
        self.__lobby.matches.append(new_match)
        # Update all players in lobby

    def __populate_default_countries(self) -> List[Country]:
        pass

    def delete_match(self, match_id):
        pass
