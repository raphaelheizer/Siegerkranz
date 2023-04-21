from source.game.networking.Network import Network
from source.object_scopes.Singleton import Singleton


class CommandProcessor(metaclass=Singleton):
    network = Network()
    # Apply COMMAND pattern
    # command queue

    # traverse command list
