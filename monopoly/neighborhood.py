
from dataclasses import dataclass

from dataclass_wizard import JSONWizard

from .property import Buildable

@dataclass
class Neighborhood(JSONWizard):
    properties: list
    color: str

if __name__ == "__main__":
    import json

    print("Creating monopoly neighborhoods")

