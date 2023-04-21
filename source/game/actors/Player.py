"""
    The player entity is not an Actor, meaning it should not be a live entity, but the vessel for the
    user on behalf of its data and non-match actions. The Country Actor is the primary vessel for actions
    in a match
"""
from queue import Queue

from source.game.command.Command import Command


class Player:
    # Player queues commands by a limit of actions by second, so we won't spam the server
    last_commands: Queue[Command]

    # TODO: Implementar algum delegate pra não depender especificamente desse websocket
    def __init__(self, p_id):
        self.p_id = p_id
