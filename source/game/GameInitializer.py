from source.game.actors.Player import Player
from source.game.command.core.CommandProcessor import CommandProcessor
from source.game.match.GameLobbyManager import GameLobbyManager
from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class GameInitializer(metaclass=Singleton):
    lobby_manager: GameLobbyManager
    network: Network
    command_processor: CommandProcessor

    async def initialize(self):
        # Load server lobby
        self.lobby_manager = GameLobbyManager()
        self.command_processor = CommandProcessor()
        self.network = Network()
        # Initializes network module with command processor
        await self.network.start(on_receive_client_message=self.process_command)

    async def process_command(self, message: str, issuer: Player):
        self.command_processor.interpret(message, issuer)
