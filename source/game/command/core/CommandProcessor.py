from asyncio import Queue
from typing import List

from source.game.actors.Player import Player
from source.game.command.core.ClassLoader import ClassLoader
from source.game.command.core.Command import Command
from source.game.command.core.CommandQueueWatcher import CommandQueueWatcher
from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class CommandProcessor(metaclass=Singleton):
    network = Network()
    available = List[Command]

    # Apply COMMAND pattern
    # command queue
    commands: Queue[Command] = []

    def __init__(self):
        self.command_queue_watcher = CommandQueueWatcher(self.commands)
        self.class_loader = ClassLoader[Command]('../command_tree')
        self.available = self.class_loader.load()

    async def interpret(self, message: str, issuer: Player) -> None:
        # Tokenize command
        root = message.split('|')
        action = root[0]
        args: dict = {}

        for idx in range(1, len(root)):
            (arg, value) = root[idx].split('=')
            args[arg] = value

        await self.execute(issuer, action, **args)

    async def execute(self, issuer: Player, action: str, **kwargs):
        current_command = [cmd for cmd in self.available if cmd.name == action][0]
        await current_command.execute(issuer, **kwargs)
