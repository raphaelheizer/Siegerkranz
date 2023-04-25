from source.game.actors.Player import Player
from source.game.command.core.Command import Command
from source.game.lobby.Lobby import Lobby


class JoinLobby(Command):

    def __init__(self):
        super().__init__()
        self.lobby = Lobby()

    async def execute(self, issuer: Player, **kwargs) -> None:
        await self.lobby.join_player(issuer)
