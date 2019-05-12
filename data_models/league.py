"""Module used to store data models for the LeagueSide API"""

from collections import namedtuple

Coordinates = namedtuple("Coordinates", "latitude longitude")


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


def _verify_coordinates(coords):
    if not 90 >= int(coords[0]) >= -90:
        raise ValueError
    if not 180 >= int(coords[1]) >= -180:
        raise ValueError
    return coords
