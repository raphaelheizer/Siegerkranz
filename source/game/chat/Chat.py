import datetime
import threading
import uuid
from typing import List, Union

from source.game.actors.Player import Player
from source.game.player.Sys import Sys


class Chat:
    connected_players: List[Player] = []
    lock = threading.Lock()

    def __init__(self, chat_id: uuid):
        self.chat_id = chat_id
        self.system = 'SYSTEM'

    async def add_player(self, player: Player):
        self.lock.acquire()
        self.connected_players.append(player)
        self.lock.release()

    async def remove_player(self, player: Player):
        self.lock.acquire()
        self.connected_players.remove(player)
        self.lock.release()

    async def broadcast(self, message: str, issuer: Player = None):
        issuer_name = await self.determine_issuer(issuer)
        for player in self.connected_players:
            await player.client.send(
                '{from:"' + issuer_name + '",message:"' + message + '",timestamp:' + str(datetime.datetime.now()) + '}')

    async def private_message(self, message: str, issuer: Union[Player, 'Sys'], receiver: Player):
        issuer_name = await self.determine_issuer(issuer)
        await receiver.client.send(
            '{from:"' + issuer_name + '",message:"' + message + '",timestamp:' + str(datetime.datetime.now()) + '}')

    async def determine_issuer(self, issuer):
        issuer_name: str
        if issuer is None:
            issuer_name = self.system
        else:
            issuer_name = issuer.name
        return issuer_name
