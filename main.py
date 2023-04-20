import asyncio

import websockets
from dotenv import load_dotenv
from websockets.legacy.server import WebSocketServerProtocol

from Bootstrap import Bootstrap
from source.game.match.MatchManager import MatchManager


async def clock_timer(websocket):
    match = MatchManager.create_match()
    await match.clock_tick(websocket)


async def listener(websocket: WebSocketServerProtocol):
    msg = await websocket.recv()
    connected: websockets.WebSocketServerProtocol = {websocket}

    for c in connected:
        print(c.state)
        print(c.debug)
        print(c.remote_address)
        print(c.id)
        print(c.is_client)
        print(c.request_headers)

    print(msg)
    await listener(websocket)


async def handler(websocket):
    while True:
        # task_clock_timer = asyncio.create_task(clock_timer(websocket))
        task_listener = asyncio.create_task(listener(websocket))
        try:
            await asyncio.gather(task_listener)
        except websockets.ConnectionClosedOK:
            break

bootstrap = Bootstrap()
load_dotenv('.app-env')


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
