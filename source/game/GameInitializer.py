from websockets.legacy.server import WebSocketServerProtocol

from source.game.command.CommandProcessor import CommandProcessor
from source.game.match.GameLobbyManager import GameLobbyManager
from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class GameInitializer(metaclass=Singleton):
    lobby_manager: GameLobbyManager
    network: Network
    command_processor: CommandProcessor

    async def initialize(self):
        # Initializes network module with command processor
        # Load server lobby
        self.lobby_manager = GameLobbyManager()
        self.command_processor = CommandProcessor()
        self.network = Network()
        await self.network.start(self.process_command)

    async def process_command(self, message: str, issuer: WebSocketServerProtocol):
        pass
