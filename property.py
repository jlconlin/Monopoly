
from dataclasses import dataclass

@dataclass
class Property():
    """
    Property 
    """
    name: str
    price: int
    rent: int

@dataclass
class BuildableProperty(Property):
    """
    This is just a property that you can build on
    """
    multipliedrent: list
    housecost: int
    nHouses: int = 0

    def __init__(self, **kwargs):
        self.multipliedrent = kwargs.pop("multipliedrent")
        self.housecost = kwargs.pop("housecost")
        super().__init__(**kwargs)
    

if __name__ == "__main__":
    print("Creating Monopoly properties")

    import json
    with open("metadata/properties.json") as pJSON:
        properties = json.load(pJSON)["properties"]

    baltic = BuildableProperty(**properties['balticave'])

