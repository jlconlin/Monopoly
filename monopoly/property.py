from dataclasses import dataclass, field
import pathlib
import json

from dataclass_wizard import JSONWizard

from . import tile

@dataclass
class Property(tile.Tile, JSONWizard):
    """
    Property 
    """
    name: str
    price: int

    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

