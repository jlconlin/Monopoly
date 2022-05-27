
from dataclasses import dataclass

from .property import BuildableProperty

@dataclass
class Neighborhood():
    properties: list
    color: str
    def __init__(self, properties, color, allProperties):
        self.color = color
        self.properties = [BuildableProperty(**allProperties[prop]) 
                           for prop in properties]

if __name__ == "__main__":
    import json

    print("Creating monopoly neighborhoods")

