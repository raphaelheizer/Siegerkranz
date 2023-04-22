from asyncio import Queue

from source.game.actors.Player import Player
from source.game.command.core.Command import Command
from source.game.command.core.CommandQueueWatcher import CommandQueueWatcher
from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class CommandProcessor(metaclass=Singleton):
    network = Network()

    # Apply COMMAND pattern
    # command queue
    commands: Queue[Command] = []

    def __init__(self):
        self.command_queue_watcher = CommandQueueWatcher(self.commands)

    def interpret(self, message: str, issuer: Player):
        # Tokenize command
        # translate to command object by searching a command tree
        # add to queue
        pass
