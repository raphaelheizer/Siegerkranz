"""
    Watches a queue and fire actions in order
"""
from asyncio import Queue

from source.game.command.core.Command import Command
from source.object_scopes.Singleton import Singleton


class CommandQueueWatcher(metaclass=Singleton):

    def __init__(self, command_queue: Queue[Command]):
        self.command_queue = command_queue

    def add(self, command: Command) -> None:
        self.command_queue.put(command)
        self.execute_pending()

    async def execute_pending(self) -> None:
        if self.command_queue.empty():
            return
        else:
            command = await self.command_queue.get()
            await command.execute()
            self.command_queue.task_done()
