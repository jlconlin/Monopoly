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
            properties = json.load(pJSON)["railroads"]

        property = monopoly.property.Property(**properties['shortlinerailroad'])
        self._testMembers(property)
        property = monopoly.property.Property.from_dict(properties['shortlinerailroad'])
        self._testMembers(property)

if __name__ == "__main__":
    unittest.main()
