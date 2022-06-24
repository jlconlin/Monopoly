import unittest

import monopoly.buildable
import monopoly.space
import monopoly.tile

class TestSpace(unittest.TestCase):
    def test_init(self):
        buildables = monopoly.buildable.makeBuildables()
        boardwalk = buildables['boardwalk']
        mediteranneanave = buildables['mediterraneanave']

        goTile = monopoly.tile.Go("go")

        space = monopoly.space.Space(
            goTile, 
            before=boardwalk,
            after=mediteranneanave)
        
        
        self.assertEqual(space.tile, goTile)
        self.assertEqual(space.name, goTile.name)
        self.assertEqual(space.before, boardwalk)
        self.assertEqual(space.after, mediteranneanave)

if __name__ == "__main__":
    unittest.main()
