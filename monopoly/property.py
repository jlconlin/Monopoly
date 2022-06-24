# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass, field
import pathlib
import json

from dataclass_wizard import JSONWizard

@dataclass
class Property(JSONWizard):
    """
    Property 
    """
    name: str
    price: int

@dataclass
class Buildable(Property):
    """
    This is just a property that you can build on
    """
    rent: int
    multipliedrent: list[int] 
    housecost: int
    nHouses: int = 0


def makeProperties(properties):
    """
    Make property objects for everything in a JSON 
    """
    with properties.open('r') as JSON:
        ps = json.load(JSON)['properties']
        return { name: value for name, value in ps.items()}
    

if __name__ == "__main__":
    import json

    print("Creating Monopoly properties")

    filename = pathlib.Path("metadata/properties.json")
    properties = makeProperties(filename)

    # baltic = BuildableProperty(**properties['balticave'])

