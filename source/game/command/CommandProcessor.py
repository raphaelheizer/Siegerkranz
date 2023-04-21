import os

from websockets.legacy.server import WebSocketServerProtocol

from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class CommandProcessor(metaclass=Singleton):
    network = Network()
    new_line = os.linesep

    async def parse_command(self, message: str, issuer: WebSocketServerProtocol):
        commands = message.replace(" ", "").split(self.new_line)

        if commands[0] == 'COMMAND':
            await CommandProcessor.parse_test(commands[1], issuer)

    @staticmethod
    async def parse_test(cmdmsg: str, issuer: WebSocketServerProtocol):
        params = cmdmsg.split('|')
        if params[0] == 'OPEN_LOBBY':
            await issuer.send('DENY')
