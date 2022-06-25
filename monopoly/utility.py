# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass
import pathlib
import json

from .property import Property

class Utility(Property):
    """
    This is just a utility. A little simpler than a buildable
    """
    pass

def makeUtilities(utilities=None):
    """
    Make utility objects for everything in the meatadata. If no argument is
    given, the utility metadata is loaded from the default.
    """
    if not utilities:
        utilities = pathlib.Path("metadata/monopoly.json")

    with utilities.open('r') as JSON:
        us = json.load(JSON)
        return {name: Utility.from_dict(value) 
                for name, value in us['utilities'].items()}


