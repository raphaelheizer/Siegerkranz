"""
    The player entity is not an Actor, meaning it should not be a live entity, but the vessel for the
    user on behalf of its data and non-match actions. The Country Actor is the primary vessel for actions
    in a match
"""

from typing import Optional

from source.game.player.Command import Command


class Player:
    last_command: Optional[Command]

    def __init__(self, p_id, websocket_client):
        self.p_id = p_id
        self.client = websocket_client
