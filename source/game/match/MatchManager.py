import threading
import uuid
from typing import List

import websockets

from source.game.actors.Country import Country
from source.game.actors.Player import Player
from source.game.chat.Chat import Chat
from source.game.match.Match import Match
from source.object_scopes.Singleton import Singleton


class MatchManager(metaclass=Singleton):
    matches: List[Match] = []
    lock = threading.Lock()

    async def create_match(self, name: str, countries: List[Country], owner: Player, players: List[Player]):
        match_uid = uuid.uuid4()
        chat_uid = uuid.uuid4()
        new_chat = Chat(chat_uid)
        new_match = Match(match_uid, name, countries, owner, new_chat, None, players)

        self.lock.acquire()
        self.matches.append(new_match)
        self.lock.release()

    async def list_matches(self, issuer: websockets.WebSocketServerProtocol):
        open_matches = [x for x in self.matches if x.is_open is True]
        issuer.send(open_matches.__repr__())
        return self.matches
