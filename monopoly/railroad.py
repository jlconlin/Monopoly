# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass
import pathlib
import json

from dataclass_wizard import JSONWizard

from .property import Property

class Railroad(Property):
    """
    This is just a railroad. A little simpler than a buildable
    """
    price: int = 200

def makeRailroads(railroads=None):
    """
    Make railroad objects for everything in the meatadata. If no argument is
    given, the railroad metadata is loaded from the default.
    """
    if not railroads:
        railroads = pathlib.Path("metadata/properties.json")

    with railroads.open('r') as JSON:
        rs = json.load(JSON)
        return {name: Railroad.from_dict(value) 
                for name, value in rs['railroads'].items()}

if __name__ == "__main__":
    print("Creating railroad collections")

    railroads = makeRailroads()