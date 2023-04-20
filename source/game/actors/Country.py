"""
    Vessel for player's actions in a match.
    This is a player driven, main class. No other entities actions should be taken for the purpose of
    progressing in a match
"""

from typing import List

from source.game.actors import State
from source.game.actors.Player import Player
from source.game.actors.Region import Region
from source.game.actors.Resources import Resources
from source.game.player.Playable import Playable


class Country(Playable):

    def __init__(self, owner: Player, name: str, region: Region, resources: Resources, states: List[State]):
        self.__owner: Player = owner
        self.name = name
        self.region = region
        self.resources = resources
        self.states = states
