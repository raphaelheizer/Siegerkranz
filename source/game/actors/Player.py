"""
    The player entity is not an Actor, meaning it should not be a live entity, but the vessel for the
    user on behalf of its data and non-match actions. The Country Actor is the primary vessel for actions
    in a match
"""
from typing import List

import websockets


class Player:
    channels: List[str]

    def __init__(self, name, client: websockets.WebSocketServerProtocol):
        self.name = name
        self.client: websockets.WebSocketServerProtocol = client

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"player_name: {self.name}, wsid: {self.client.id}"
