import argparse
import pathlib

from monopoly.neighborhood import Neighborhood

if __name__ == "__main__":
    import json

    print("Monopoly")

    parser = argparse.ArgumentParser(description='Play monopoly')
    parser.add_argument('--properties', type=pathlib.Path,
                        default="metadata/properties.json",
                        help="JSON description of the properties")
    parser.add_argument('--neighborhoods', type=pathlib.Path,
                        default="metadata/neighborhoods.json",
                        help="JSON description of the neighborhoods")

    args = parser.parse_args()
