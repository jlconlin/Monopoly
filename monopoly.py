
from monopoly.neighborhood import Neighborhood

if __name__ == "__main__":
    import json

    print("Monopoly")

    with open("metadata/properties.json") as pJSON:
        properties = json.load(pJSON)["properties"]

    neighborhoods = {}
    with open("metadata/neighborhoods.json") as nJSON:
        for name, hood in  json.load(nJSON)['neighborhoods'].items():
            neighborhoods[name] = Neighborhood(**hood, allProperties=properties)
