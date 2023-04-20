import datetime

from source.game.actors.Player import Player


class Command:

    def __init__(self, value: str, owner: Player):
        self.__value = value
        self.__owner = owner
        # Order player actions by time
        self.time_stamp = datetime.datetime.now()
