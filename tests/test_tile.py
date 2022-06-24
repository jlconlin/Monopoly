import unittest
import pathlib

import monopoly.tile

class TestTile(unittest.TestCase):
    pass


class TestmakeTiles(unittest.TestCase):
    def _assertNames(self, tiles):
        referenceNames = [
            "go",
            "communitychest",
            "incometax",
            "chance",
            "jail",
            "justvisiting",
            "freeparking",
            "gotojail",
            "luxurytax"]
        self.assertEqual(referenceNames, list(tiles.keys()))

    def test_makeTiles(self):
        tiles = monopoly.tile.makeTiles()
        self._assertNames(tiles)
        filename = pathlib.Path("metadata/tiles.json")
        tiles = monopoly.tile.makeTiles()
        self._assertNames(tiles)


if __name__ == "__main__":
    unittest.main()
