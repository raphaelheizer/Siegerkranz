"""
    Representation of a server's lobby and all matches available at a time. It should be unique in a server
"""

from typing import List

from source.game.actors.Player import Player
from source.game.chat.Chat import Chat
from source.game.match.MatchManager import MatchManager
from source.object_scopes.Singleton import Singleton


class Lobby(metaclass=Singleton):
    matches = MatchManager().matches

    def __init__(self, joined_players: List[Player], chat: Chat):
        self.__joined_players: List[Player] = joined_players
        self.chat = chat

    async def join_player(self, player: Player):
        self.__joined_players.append(player)
        self.chat.connected_players.append(player)
        # LISTEN TO LOBBY STATE AND NOTIFY

    async def remove_player(self, player: Player):
        self.__joined_players.remove(player)
        await self.chat.remove_player(player)

    async def broadcast_message(self, message: str, issuer: Player):
        await self.chat.broadcast(message, issuer)

    async def private_message(self, message: str, issuer: Player, receiver: Player):
        await self.chat.private_message(message, issuer, receiver)
