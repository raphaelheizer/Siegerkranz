import datetime
from abc import ABCMeta, abstractmethod

from source.game.actors.Player import Player


class Command(metaclass=ABCMeta):
    finished = False
    name: str

    def __init__(self):
        self.time_stamp = datetime.datetime.now()

    @abstractmethod
    async def execute(self, issuer: Player, **kwargs) -> None:
        pass
