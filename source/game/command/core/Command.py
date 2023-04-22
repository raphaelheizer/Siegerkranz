import datetime
from abc import ABCMeta, abstractmethod

from source.game.actors.Player import Player


class Command(metaclass=ABCMeta):
    finished = False

    def __init__(self, issuer: Player):
        self.time_stamp = datetime.datetime.now()
        self.__issuer = issuer

    async def handle(self):
        await self.execute()
        self.finished = True

    @abstractmethod
    async def execute(self) -> None:
        pass
