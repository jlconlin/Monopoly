# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Space():
    tile: Tile
    left: Space = None
    right: Space = None

if __name__ == "__main__":
    print("Making a monopoly space")
