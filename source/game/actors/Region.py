from source.game.actors.Continent import Continent


class Region:

    def __init__(self, name: str, continent: Continent):
        self.name = name
        self.continent = continent
