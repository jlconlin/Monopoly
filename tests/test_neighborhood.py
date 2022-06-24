import unittest
import json
import pathlib

import monopoly.neighborhood
import monopoly.property

class TestNeighborhood(unittest.TestCase):
    def setUp(self):
        self.properties = monopoly.property.makeProperties()

    def _testMembers(self, neighborhood):
        self.assertEqual(neighborhood.color, "Purple")
        self.assertEqual(neighborhood.properties[0],
                         self.properties["mediterraneanave"])
        self.assertEqual(neighborhood.properties[1],
                         self.properties["balticave"])

    def test_init(self):
        purple = {
            "color": "Purple",
            "properties": [ "mediterraneanave", "balticave" ]
        }
        neighborhood = monopoly.neighborhood.Neighborhood(
            self.properties, **purple)
        self._testMembers(neighborhood)

    def test_init_fromJSON(self):
        filename = pathlib.Path("metadata/neighborhoods.json")
        with filename.open('r') as JSON:
            neighborhoods = json.load(JSON)["neighborhoods"]
        neighborhood = monopoly.neighborhood.Neighborhood(
            self.properties, **neighborhoods['Purple'])


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # unittest.main()
