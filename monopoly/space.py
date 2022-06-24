# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Space():
    tile: Tile
    before: Space = None
    after: Space = None

    @property
    def name(self):
        return self.tile.name

if __name__ == "__main__":
    print("Making a monopoly space")
