from dataclasses import dataclass, field
import pathlib
import json

from .tile import Tile

@dataclass
class Property(Tile):
    """
    Property 
    """
    price: int

    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

