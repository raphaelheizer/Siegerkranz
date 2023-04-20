from abc import ABC
from typing import Optional

from source.game.actors.Player import Player


class Playable(ABC):
    __player: Optional[Player]

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if player is None:
            """ TODO: remove ownership of all player actors"""
        else:
            self.__player = player
