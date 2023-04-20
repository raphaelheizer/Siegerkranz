"""
    The player entity is not an Actor, meaning it should not be a live entity, but the vessel for the
    user on behalf of its data and non-match actions. The Country Actor is the primary vessel for actions
    in a match
"""

from typing import List

import websockets

from source.game.player.Command import Command


class Player:
    last_commands: List[Command]

    # TODO: Implementar algum delegate pra não depender especificamente desse websocket
    def __init__(self, p_id, websocket_client: websockets.WebSocketServerProtocol):
        self.p_id = p_id
        self.client = websocket_client
