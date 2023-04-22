import datetime
import threading
import uuid
from typing import List

from source.game.actors.Player import Player


class Chat:
    connected_players: List[Player] = []
    lock = threading.Lock()

    def __init__(self, chat_id: uuid):
        self.chat_id = chat_id

    async def add_player(self, player: Player):
        self.lock.acquire()
        self.connected_players.append(player)
        self.lock.release()

    async def remove_player(self, player: Player):
        self.lock.acquire()
        self.connected_players.remove(player)
        self.lock.release()

    async def broadcast(self, message: str, issuer: Player):
        for player in self.connected_players:
            await player.client.send(message)

    @staticmethod
    async def private_message(message: str, issuer: Player, receiver: Player):
        receiver.client.send("{from:" + issuer.name + ',message:' + message + '}',
                             'timestamp:' + str(datetime.datetime.now()))
