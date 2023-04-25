import asyncio

from dotenv import load_dotenv

from source.game.GameInitializer import GameInitializer

load_dotenv('.app-env')
game_initializer: GameInitializer


async def main():
    global game_initializer
    game_initializer = GameInitializer()
    await game_initializer.initialize()


if __name__ == "__main__":
    asyncio.run(main())
