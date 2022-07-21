"""
Tiles are the different things that can go on each Space. There are several
unique Tiles that have their own classes here.
"""

# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass
import sys
import inspect
import pathlib
import json

from dataclass_wizard import JSONWizard

from .space import Space

@dataclass
class Tile(JSONWizard):
    name: str

class Go(Tile):
    pass

class _Card(Tile):
    pass

class Chance(_Card):
    pass

class CommunityChest(_Card):
    pass

class FreeParking(Tile):
    pass

class GotoJail(Tile):
    pass

class Jail(Tile):
    pass

class _Tax(Tile):
    pass

class LuxuryTax(_Tax):
    pass

class IncomeTax(_Tax):
    pass

class JustVisiting(Tile):
    pass

def makeTiles(tiles=None):
    """
    """
    classes = {name: Class for name, Class in 
               inspect.getmembers(sys.modules[__name__], inspect.isclass)}

    if not tiles:
        tiles = pathlib.Path("metadata/monopoly.json")

    allTiles = {}
    with tiles.open('r') as JSON:
        ts = json.load(JSON)['tiles']
        for name, value in ts.items():
            try:
                allTiles[name] = classes.get(value['type']).from_dict(value)
            except TypeError as te:
                print("Don't know how to create a tile of type: {}"
                      .format(value['type']))
                raise te

    return allTiles
    
if __name__ == "__main__":
    print("Creating monopoly tiles")

    tiles = makeTiles()
