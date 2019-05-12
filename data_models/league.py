"""Module used to store data models for the LeagueSide API"""

from collections import namedtuple

Coordinates = namedtuple("Coordinates", "latitude longitude")

# TODO: Add coordinate validation -90/90 - -180/180
class League:
    """An instance of a league contains a name, price required for sponsorship, and a geographic
    position denoted by a Latitude/Longitude pair"""

    def __init__(self, league_name, price, coords):
        self.name = league_name
        self.price = price
        self.coordinates = Coordinates(*coords)

    def asdict(self):
        """Returns instance of the object as a Python dictionary"""
        return {"name": self.name, "price": self.price, "coordinates": self.coordinates}

    def __repr__(self):
        return f"{self.name} -- Price: {self.price}, {self.coordinates}"
