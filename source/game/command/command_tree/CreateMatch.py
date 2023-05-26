from source.game.actors.Player import Player
from source.game.command.core.Command import Command
from source.game.match.GameLobbyManager import GameLobbyManager


class CreateMatch(Command):
    lobby_manager = GameLobbyManager()

    async def execute(self, issuer: Player, **kwargs) -> None:
        await self.lobby_manager.create_match(issuer, kwargs.get('name'))
