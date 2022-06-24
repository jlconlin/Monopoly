import unittest
import json
import pathlib

import monopoly.property

class TestProperty(unittest.TestCase):
    def _testMembers(self, property):
        self.assertEqual(property.name, "Short Line Railroad")
        self.assertEqual(property.price, 200)

    def test_init(self):
        shortLine = {
            "name": "Short Line Railroad",
            "price": 200
        }

        property = monopoly.property.Property(**shortLine)
        self._testMembers(property)

    def test_init_fromJSON(self):
        with open("metadata/properties.json") as pJSON:
            properties = json.load(pJSON)["properties"]

        property = monopoly.property.Property(**properties['shortlinerailroad'])
        self._testMembers(property)
        property = monopoly.property.Property.from_dict(properties['shortlinerailroad'])
        self._testMembers(property)

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

        buildable = monopoly.property.Buildable(**boardwalk)
        self.assertEqual(buildable.name, boardwalk['name'])
        self.assertEqual(buildable.price, boardwalk['price'])
        self.assertEqual(buildable.rent, boardwalk['rent'])
        self.assertEqual(buildable.multipliedrent, boardwalk['multipliedrent'])
        self.assertEqual(buildable.housecost, boardwalk['housecost'])

class TestmakeProperties(unittest.TestCase):
    def _assertNames(self, properties):
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
            "boardwalk",
            "electriccompany",
            "waterworks",
            "readingrailroad",
            "pennsylvaniarailroad",
            "borailroad",
            "shortlinerailroad"]
        self.assertEqual(referenceNames, list(properties.keys()))

    def test_makeProperties(self):
        properties = monopoly.property.makeProperties()
        self._assertNames(properties)
        filename = pathlib.Path("metadata/properties.json")
        properties = monopoly.property.makeProperties(filename)
        self._assertNames(properties)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # unittest.main()
