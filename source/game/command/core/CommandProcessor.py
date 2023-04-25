from asyncio import Queue

from source.game.actors.Player import Player
from source.game.command.command_tree.DisonnectFromAll import DisconnectFromAll
from source.game.command.command_tree.JoinLobby import JoinLobby
from source.game.command.command_tree.SendMessageLobby import SendMessageLobby
from source.game.command.core.Command import Command
from source.game.command.core.CommandQueueWatcher import CommandQueueWatcher
from source.object_scopes.Singleton import Singleton


class CommandProcessor(metaclass=Singleton):
    # Can't think of a better way right now. I'm sandboxing this game engine to further improve
    # my knowledge about basic game server mechanics
    available = {
        'DISCON_ALL': DisconnectFromAll(),
        'JOIN_LOBBY': JoinLobby(),
        'SND_MSG_LB': SendMessageLobby()
    }

    # Apply COMMAND pattern
    # command queue
    commands: Queue[Command] = []

    def __init__(self):
        self.command_queue_watcher = CommandQueueWatcher(self.commands)

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
        current_command: Command
        try:
            current_command = self.available[action]
            await current_command.execute(issuer, **kwargs)
        except KeyError:
            print(f'Unknown command "{str(action)}"')
