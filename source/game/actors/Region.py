"""
    The region a given country is localized in
"""

from source.game.actors.Continent import Continent


class Region:

    def __init__(self, region_id, name: str, continent: Continent):
        self.__region_id = region_id  # Isso é o que vai indicar onde está no mapa
        self.name = name
        self.continent = continent
