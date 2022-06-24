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

    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

