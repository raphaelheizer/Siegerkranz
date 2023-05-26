"""
    Representation of a server's lobby and all matches available at a time. It should be unique in a server
"""
import uuid
from typing import List

from source.game.actors.Player import Player
from source.game.chat.Chat import Chat
from source.game.match.MatchManager import MatchManager
from source.game.player.Sys import Sys
from source.object_scopes.Singleton import Singleton


class Lobby(metaclass=Singleton):
    matches = MatchManager().matches

    def __init__(self):
        self.joined_players: List[Player] = []
        self.chat = Chat(uuid.uuid4())

    async def join_player(self, player: Player):
        if self.joined_players.__contains__(player):
            await self.chat.private_message('Player already in lobby', Sys(), player)
            return
        else:
            self.joined_players.append(player)
            self.chat.connected_players.append(player)
            await self.chat.broadcast(f'Player {player.name} joined the lobby', player)
            await player.client.send('{matches:' + self.matches.__repr__() + '}')

    async def remove_player(self, player: Player):
        self.joined_players.remove(player)
        await self.chat.remove_player(player)
        await self.chat.broadcast(f'Player {player} has left the game', player)
