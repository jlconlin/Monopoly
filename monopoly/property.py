
from dataclasses import dataclass
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
    multipliedrent: list
    housecost: int
    nHouses: int = 0

if __name__ == "__main__":
    import json

    print("Creating Monopoly properties")

    with open("metadata/properties.json") as pJSON:
        properties = json.load(pJSON)["properties"]

    # baltic = BuildableProperty(**properties['balticave'])

