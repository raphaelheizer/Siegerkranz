from source.game.GameContext import GameContext
from source.game.GameState import GameState


class MatchManager:

    @staticmethod
    def create_match():
        context = GameContext()
        game_state = GameState(context)
        print('created')
        return game_state
