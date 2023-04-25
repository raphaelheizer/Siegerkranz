from source.game.actors.Player import Player
from source.game.command.core.Command import Command
from source.game.lobby.Lobby import Lobby


class SendMessageLobby(Command):

    def __init__(self):
        super().__init__()
        self.lobby = Lobby()

    async def execute(self, issuer: Player, **kwargs) -> None:
        msg = kwargs.get('message')
        print(f'chat - {issuer.name}: {msg}')
        await self.lobby.chat.broadcast(msg, issuer)
