from source.game.actors.Player import Player
from source.game.command.core.Command import Command


class JoinLobby(Command):
    async def execute(self, issuer: Player, **kwargs) -> None:
        self.name = 'JOIN_LOBBY'
        print('Command executed! Args= ' + kwargs.__str__())
