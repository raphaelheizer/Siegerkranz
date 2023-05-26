from source.game.actors.Player import Player
from source.game.command.core.Command import Command
from source.game.lobby.Lobby import Lobby
from source.game.match.MatchManager import MatchManager


class DisconnectFromAll(Command):
    matches = MatchManager()  # TODO: Encontrar aonde o jogador está conectado e desconectar ele
    lobby = Lobby()

    async def execute(self, issuer: Player, **kwargs) -> None:
        await self.lobby.remove_player(issuer)
