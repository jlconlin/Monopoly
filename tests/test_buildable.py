import unittest
import json
import pathlib

import monopoly.buildable

class TestBuildable(unittest.TestCase):
    def test_init(self):

        boardwalk = {
            "name": "Boardwalk",
            "price": 400,
            "rent": 50,
            "multipliedrent": [
                200,
                600,
                1400,
                1700,
                2000
            ],
            "housecost": 200
        }

        buildable = monopoly.buildable.Buildable(**boardwalk)
        self.assertEqual(buildable.name, boardwalk['name'])
        self.assertEqual(buildable.price, boardwalk['price'])
        self.assertEqual(buildable.rent, boardwalk['rent'])
        self.assertEqual(buildable.multipliedrent, boardwalk['multipliedrent'])
        self.assertEqual(buildable.housecost, boardwalk['housecost'])

class TestmakeBuildables(unittest.TestCase):
    def _assertNames(self, buildables):
        referenceNames = [
            "mediterraneanave",
            "balticave",
            "orientalave",
            "vermontave",
            "connecticutave",
            "stcharlesplace",
            "statesave",
            "virginiaave",
            "stjamesplace",
            "tennesseeave",
            "newyorkave",
            "kentuckyave",
            "indianaave",
            "illinoisave",
            "atlanticave",
            "ventnorave",
            "marvingardens",
            "pacificave",
            "northcarolinaave",
            "pennsylvaniaave",
            "parkplace",
            "boardwalk"]
            
        self.assertEqual(referenceNames, list(buildables.keys()))

    def test_makebuildables(self):
        buildables = monopoly.buildable.makeBuildables()
        self._assertNames(buildables)
        filename = pathlib.Path("metadata/properties.json")
        buildables = monopoly.buildable.makeBuildables(filename)
        self._assertNames(buildables)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # unittest.main()
