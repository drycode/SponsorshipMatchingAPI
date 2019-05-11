"""This file provides methods used by to access the MongoDB database by the Flask
Application. """

from collections import namedtuple
from geopy.distance import geodesic
from mongo.mongo_config import DB, LEAGUES_COLLECTION as L_COL


Coordinates = namedtuple("Coordinates", "latitude longitude")

# TODO: consider putting League class in its own file, accessible by other interfaces
# TODO: consider doing some sort of Coordinate validation
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


def get_leagues(total_budget, search_radius, central_location, collection=L_COL):
    """Returns a list of leagues to sponsor within a given budget and location"""
    # Local leagues is a list of leagues within a given search radius
    local_leagues = _compile_local_leagues(search_radius, central_location, collection)
    local_leagues.sort(key=lambda x: x["price"])

    # Selected leagues are leagues that were selected for sponsorship given the
    # selection parameters (total budget, location, etc.)
    selected_leagues = []
    for league in local_leagues:

        remaining_budget = total_budget
        total_budget -= league["price"]
        if total_budget >= 0:
            selected_leagues.append(
                {
                    "name": league["name"],
                    "price": league["price"],
                    "coordinates": league["coordinates"],
                }
            )
        else:
            break
    return selected_leagues, remaining_budget


def add_league_to_db(league_name, price, coordinates, collection=L_COL):
    """Adds a league to the database if one with the same name does not exist,
    otherwise, it updates the object with league_name as the unique identifier"""
    existing = collection.find_one({"name": league_name})
    print(existing)

    new_league = League(league_name, price, coordinates)
    if existing:
        collection.update_one({"_id": existing["_id"]}, {"$set": new_league.asdict()})
    else:
        collection.insert_one(new_league.asdict())
    return new_league


def verify_active_db(collection=L_COL, DB=DB):
    """Checks the existence/accessibility of the MongoDB instance"""
    return collection.name in DB.list_collection_names()


def _compile_local_leagues(search_radius, central_location, collection):
    """Returns a list of leagues that fit within the given location parameters"""
    all_leagues = collection.find()
    local_leagues = []
    for league in all_leagues:

        # Checks the distance of the league's coordinates against the given location
        # If within the given search radius, the league is appended to the returned list
        if geodesic(central_location, league["coordinates"]).miles <= search_radius:
            local_leagues.append(league)
    return local_leagues
