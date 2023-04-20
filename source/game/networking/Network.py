import asyncio
import os

import websockets

from Bootstrap import Bootstrap

bootstrap = Bootstrap()


class Network:
    server = None

    async def start_server(self):
        port = os.getenv('SERVER_PORT', 5256)
        async with websockets.serve(self.handler, "", port) as server:
            self.server = server
            await asyncio.Future()  # game loop

    async def handler(self):
        while True:
            task_listener = asyncio.create_task(self.message_listener())
            try:
                await asyncio.gather(task_listener)
            except websockets.ConnectionClosedOK:
                break

    async def message_listener(self):
        msg = await self.server.recv()
        # interpret messages
        await self.message_listener()
