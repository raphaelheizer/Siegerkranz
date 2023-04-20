import asyncio
import uuid

from source.game.GameContext import GameContext


class GameState:
    game_id: uuid
    game_time: int = 0

    def __init__(self, game_context: GameContext):
        self.game_context = game_context
        self.game_id = uuid.uuid4()

    async def clock_tick(self, websocket):
        await asyncio.sleep(1)
        self.game_time += 1
        print(f'gameid: {self.game_id} --> time: ' + str(self.game_time))
        if websocket.open:
            await websocket.send(f'time: {str(self.game_time)}')
        else:
            print("connection closed. Can't comply")
        await self.clock_tick(websocket)
