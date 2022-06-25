import unittest
import pathlib

import monopoly.utility

class TestUtility(unittest.TestCase):
    def _testMembers(self, utility):
        self.assertEqual(utility.name, "Reading utility")
        self.assertEqual(utility.price, 200)

    def test_init(self):
        reading = {
            "name": "Reading utility",
            "price": 200
        }
        utility = monopoly.utility.Utility(**reading)

class TestmakeUtilities(unittest.TestCase):
    def _assertNames(self, utilities):
        referenceNames = [
            "electriccompany",
            "waterworks"
        ]
        self.assertEqual(referenceNames, list(utilities.keys()))
    def test_makeutilities(self):
        utilities = monopoly.utility.makeUtilities()
        self._assertNames(utilities)
        filename = pathlib.Path("metadata/monopoly.json")
        utilities = monopoly.utility.makeUtilities(filename)
        self._assertNames(utilities)

if __name__ == "__main__":
    unittest.main()


