import datetime
from typing import Callable

from source.game.actors.Player import Player


class Command:
    finished = False

    def __init__(self, issuer: Player, action: Callable = None):
        self.__action = action
        self.time_stamp = datetime.datetime.now()
        self.__issuer = issuer

    @property
    def action(self) -> Callable:
        return self.action

    @action.setter
    def action(self, action: Callable):
        self.action = action

    async def execute(self) -> None:
        if self.__action is None:
            print('No action executed for player' + self.__issuer.name)
            return
        await self.action()
        self.finished = True
