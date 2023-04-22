import asyncio
import datetime
from typing import Callable, List

import websockets
from websockets.legacy.server import WebSocketServerProtocol

from source.game.actors.Player import Player
from source.object_scopes.Singleton import Singleton


class Network(metaclass=Singleton):
    on_message_callback: Callable = None
    __connections: List[websockets.WebSocketServerProtocol] = list()
    server: websockets = websockets
    players: List[Player] = []

    @property
    def connections(self):
        return self.__connections

    async def listener(self, websocket: WebSocketServerProtocol):
        message = await websocket.recv()
        await self.on_message_callback(message, websocket)
        await self.listener(websocket)

    async def handler(self, websocket: WebSocketServerProtocol):
        while True:
            task_listener = asyncio.create_task(self.listener(websocket))
            connection: WebSocketServerProtocol = websocket
            self.connections.append(connection)
            joined_player = Player(websocket.request_headers['player_name'], connection)
            self.players.append(joined_player)
            print(f"Player {connection.request_headers['player_name']} joined the server at {datetime.datetime.now()}")
            print(f'Connected players: {self.players.__repr__()}')
            try:
                # Any server-sent actions must be async and joined in asyncio.gather
                await asyncio.gather(task_listener)
            except websockets.ConnectionClosedOK:
                self.connections.remove(connection)
                player = [p for p in self.players if p.client.id == connection.id]
                self.players.remove(player[0])
                print(f"Player {connection.request_headers['player_name']} disconnected at {datetime.datetime.now()}")
                break

    async def start(self, on_message_callback: Callable):
        async with websockets.serve(self.handler, "", 8001):
            self.on_message_callback = on_message_callback
            await asyncio.Future()  # Network Game Loop
