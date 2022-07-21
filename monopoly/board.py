import itertools
import json
import pathlib

from dataclasses import dataclass

from . import buildable, tile, railroad, utility, space

def getAllTiles(buildables=None, railroads=None, utilities=None, tiles=None):
    """
    Return all the "tiles" available for the game. These include:
        - buildable properties
        - railroads
        - utilities
        - plain tiles
    """
    builds = buildable.makeBuildables(buildables)
    railroads = railroad.makeRailroads(railroads)
    utilities = utility.makeUtilities(utilities)
    tiles = tile.makeTiles(tiles)

    return {**builds, **railroads, **utilities, **tiles}
    

@dataclass
class Board():
    """
    Game board
    """
    tiles: list[space.Space]

    def __post_init(self):
        before = self.tiles[-1]
        for tile in self.tiles:
            tile.before = before
            before.after = tile
            before = tile


if __name__ == "__main__":
    print("Creating a monopoly board")

    filename = pathlib.Path("metadata/board.json")
    with filename.open('r') as JSON:
        US = json.load(JSON)['US']
    tiles = getAllTiles()
    board = Board([tiles[tile] for tile in US])

