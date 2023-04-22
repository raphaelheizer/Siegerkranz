import datetime
from typing import Callable


class Command:
    __action: Callable
    finished = False

    @property
    def action(self) -> Callable:
        return self.action

    @action.setter
    def action(self, action: Callable):
        self.action = action

    def __init__(self):
        self.time_stamp = datetime.datetime.now()

    async def execute(self) -> None:
        await self.action()
        self.finished = True
