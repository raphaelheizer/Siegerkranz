import asyncio
import datetime
from typing import Callable, List

import websockets
from websockets.legacy.server import WebSocketServerProtocol

from source.game.actors.Player import Player
from source.game.command.core.CommandProcessor import CommandProcessor
from source.object_scopes.Singleton import Singleton


class Network(metaclass=Singleton):
    on_message_callback: Callable = None
    __connections: List[websockets.WebSocketServerProtocol] = list()
    server: websockets = websockets
    players: List[Player] = []
    command_processor = CommandProcessor()

    @property
    def connections(self):
        return self.__connections

    async def listener(self, websocket: WebSocketServerProtocol):
        message = await websocket.recv()
        issuer: Player = [p for p in self.players if p.client.id == websocket.id][0]
        await self.on_message_callback(message, issuer)
        await self.listener(websocket)

    async def handler(self, websocket: WebSocketServerProtocol):
        while True:
            task_listener = asyncio.create_task(self.listener(websocket))
            connection: WebSocketServerProtocol = websocket
            self.connections.append(connection)
            joined_player = Player(websocket.request_headers['player_name'], connection)
            self.players.append(joined_player)
            print(f"Player {connection.request_headers['player_name']} joined the server at {datetime.datetime.now()}")
            try:
                # Any server-sent actions must be async and joined in asyncio.gather
                await asyncio.gather(task_listener)
            except websockets.ConnectionClosedOK:
                self.connections.remove(connection)
                players = [p for p in self.players if p.client.id == connection.id]
                self.players.remove(players[0])
                await self.command_processor.execute(players[0], 'DISCON_ALL', **{})
                print(f"Player {connection.request_headers['player_name']} disconnected at {datetime.datetime.now()}")
                break

    async def start(self, on_receive_client_message: Callable):
        port = 5266
        print('Server started at port ' + port.__str__() + ' 👍')
        async with websockets.serve(self.handler, "", port):
            self.on_message_callback = on_receive_client_message
            await asyncio.Future()  # Network Game Loop 👍
