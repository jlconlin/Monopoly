import unittest
import pathlib
import json

import monopoly.board

class TestBoard(unittest.TestCase):
    def setUp(self):
        filename = pathlib.Path("metadata/board.json")
        with filename.open('r') as JSON:
            US = json.load(JSON)['US']
        allTiles = monopoly.board.getAllTiles()
        self.tiles = [allTiles[tile] for tile in US]

    def test_init(self):
        board = monopoly.board.Board(self.tiles)

        refBeforeNames = [tile.name for tile in self.tiles]
        refBeforeNames.insert(0, refBeforeNames.pop())

        beforeNames = [tile.before.name for tile in board.tiles]
        self.assertEqual(refBeforeNames, beforeNames)


if __name__ == "__main__":
    unittest.main()
