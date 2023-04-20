from source.game.actors.Player import Player


class State:

    def __init__(self, name: str, owner: Player):
        self.name = name
        self.__owner = owner
