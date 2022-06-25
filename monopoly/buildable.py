# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass
import pathlib
import json

from . import property

@dataclass
class Buildable(property.Property):
    """
    This is just a property that you can build on
    """
    rent: int
    multipliedrent: list[int] 
    housecost: int
    nHouses: int = 0

def makeBuildables(buildables=None):
    """
    Make property objects for everything in a JSON. If no argument is given, the
    property metadata is loaded from the default
    """
    if not buildables:
        buildables = pathlib.Path("metadata/monopoly.json")

    with buildables.open('r') as JSON:
        bs = json.load(JSON)
        return { name: Buildable.from_dict(value) 
                   for name, value in bs['buildables'].items()}

if __name__ == "__main__":
    print("Creating Monopoly buildables")

    buildables = makeBuildables()
