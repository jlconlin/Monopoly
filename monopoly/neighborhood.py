# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass
import pathlib
import json

from .property import Buildable

@dataclass
class Neighborhood():
    properties: list[str]
    color: str

    def __init__(self, globalProperties, color, properties):
        self.color = color
        self.properties = [globalProperties[name] for name in properties]

def buildNeighborhoods(properties, neighborhoods=None):
    """
    Create all the neighborhoods described in a JSON file. If no argument is
    given, the neighborhood metadata is loaded from the default.
    """
    if not neighborhoods:
        neighborhoods = pathlib.Path("metadata/neighborhoods.json")

    with neighborhoods.open('r') as JSON:
        ns = json.load(JSON)['neighborhoods']
        return { name: Neighborhood(properties, **value)
                for name, value in ns.items() }

if __name__ == "__main__":
    import json

    print("Creating monopoly neighborhoods")

