# Player driven, main class. Serves as vessel to all player actions
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
