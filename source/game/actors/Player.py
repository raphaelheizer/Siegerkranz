from typing import Optional

from source.game.player.Command import Command


class Player:
    last_command: Optional[Command]

    def __init__(self, p_id, websocket_client):
        self.p_id = p_id
        self.client = websocket_client
