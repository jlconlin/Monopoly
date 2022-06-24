import unittest
import pathlib

import monopoly.railroad

class TestRailroad(unittest.TestCase):
    def _testMembers(self, railroad):
        self.assertEqual(railroad.name, "Reading Railroad")
        self.assertEqual(railroad.price, 200)

    def test_init(self):
        reading = {
            "name": "Reading Railroad",
            "price": 200
        }
        railroad = monopoly.railroad.Railroad(**reading)

class TestmakeRailroads(unittest.TestCase):
    def _assertNames(self, railroads):
        referenceNames = [
            "readingrailroad",
            "pennsylvaniarailroad",
            "borailroad",
            "shortlinerailroad"
        ]
        self.assertEqual(referenceNames, list(railroads.keys()))
    def test_makeRailroads(self):
        railroads = monopoly.railroad.makeRailroads()
        self._assertNames(railroads)
        filename = pathlib.Path("metadata/properties.json")
        railroads = monopoly.railroad.makeRailroads(filename)
        self._assertNames(railroads)

if __name__ == "__main__":
    unittest.main()

