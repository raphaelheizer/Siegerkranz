import asyncio
import datetime
from typing import Callable, List

import websockets
from websockets.legacy.server import WebSocketServerProtocol

from source.object_scopes.Singleton import Singleton


class Network(metaclass=Singleton):
    on_message_callback: Callable = None
    __connections: List[websockets.WebSocketServerProtocol] = list()
    server: websockets = websockets

    @property
    def connections(self):
        return self.__connections

    async def listener(self, websocket: WebSocketServerProtocol):
        message = await websocket.recv()
        await self.on_message_callback(message, websocket)
        await self.listener(websocket)

    async def handler(self, websocket):
        while True:
            task_listener = asyncio.create_task(self.listener(websocket))
            connection: WebSocketServerProtocol = websocket
            self.connections.append(connection)
            print(f"Player {connection.request_headers['playername']} has just joined the server")
            try:
                # Any server-sent actions must be async and joined in asyncio.gather
                await asyncio.gather(task_listener)
            except websockets.ConnectionClosedOK:
                self.connections.remove(connection)
                print(f"Player {connection.request_headers['playername']} disconnected at {datetime.datetime.now()}")
                break

    async def start(self, on_message_callback: Callable):
        async with websockets.serve(self.handler, "", 8001):
            self.on_message_callback = on_message_callback
            await asyncio.Future()  # Network Game Loop
