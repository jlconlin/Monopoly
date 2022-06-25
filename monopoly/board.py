import itertools
import json
import pathlib

from . import buildable, tile, railroad

def overlapper(seq, size):
    return (seq[pos:pos + size]
            for pos in range(0, len(seq)))


def getAllTiles(tiles=None):
    """
    Return all the "tiles" available for the game. These include:
        - buildable properties
        - railroads
        - utilities
        - plain tiles
    """
    if not tiles:
        tiles = pathlib.Path("metadata/monopoly.json")
    builds = buildable.makeBuildables(tiles)
    railroads = railroad.makeRailroads(tiles)


if __name__ == "__main__":
    print("Creating a monopoly board")

    filename = pathlib.Path("metadata/board.json")
    with filename.open('r') as JSON:
        US = json.load(JSON)['US']

    for pre, space, nex in overlapper(US, 3):
        space.pre = pre
        space.nex = nex

