"""
    Manages the state of all the game matches. Must be unique
"""
import uuid
from typing import List

from source.game.actors.Country import Country
from source.game.actors.Player import Player
from source.game.chat.Chat import Chat
from source.game.lobby.Lobby import Lobby
from source.game.match.Match import Match
from source.object_scopes.Singleton import Singleton


class GameLobbyManager(metaclass=Singleton):
    def __init__(self):
        # TODO: Load if there is any running matches in database
        # TODO: Load if there is any chat in course. Else create one
        self.__lobby = Lobby([], Chat(uuid.uuid4()))

    def create_match(self, owner: Player, name: str):
        # Generate random ID for the match
        match_uid = uuid.uuid4()
        # If we're creating a match, a new chat will be required to be created anew each time
        new_match = Match(match_uid, name, self.__populate_countries(), owner, Chat(uuid.uuid4()), None, [])
        self.__lobby.matches.append(new_match)
        # TODO: Update all players in lobby

    def __populate_countries(self) -> List[Country]:
        pass

    def delete_match(self, match_id):
        pass
