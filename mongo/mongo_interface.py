# from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from collections import namedtuple
from mongo.mongo_config import leagues_collection

# Queries all available leagues in a collection

coordinates = namedtuple("Coordinates", "latitude longitude")


class League:
    def __init__(self, league_name, price, coords):
        self.name = league_name
        self.price = price
        self.coordinates = coordinates(*coords)

    def asdict(self):
        return {"name": self.name, "price": self.price, "coordinates": self.coordinates}

    def __repr__(self):
        return f"{self.name}: Price: {self.price}, {self.coordinates}"


def get_leagues(total_budget, search_radius, central_location):
    """Returns a list of leagues to sponsor within a given budget and location"""
    # Local leagues is a list of leagues within a given search radius

    local_leagues = _compile_local_leagues(search_radius, central_location)
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


def add_league_to_db(league_name, price, coordinates):
    existing = leagues_collection.find_one({"name": league_name})
    print(existing)

    new_league = League(league_name, price, coordinates)
    if existing:
        leagues_collection.update_one(
            {"_id": existing["_id"]}, {"$set": new_league.asdict()}
        )
    else:
        leagues_collection.insert_one(new_league.asdict())
    return new_league


def _compile_local_leagues(search_radius, central_location):
    """Returns a list of leagues that fit within the given location parameters"""
    all_leagues = leagues_collection.find()
    local_leagues = []
    for league in all_leagues:

        # Checks the distance of the league's coordinates against the given location
        # If within the given search radius, the league is appended to the returned list
        if geodesic(central_location, league["coordinates"]).miles <= search_radius:
            local_leagues.append(league)
    return local_leagues


# selected_leagues, remaining_budget = get_leagues(total_budget, 5, central_location)
# [print(league["name"]) for league in selected_leagues]
# print(remaining_budget)

# add_league_to_db("The Raptors", 5400, [40.0276623852143, -75.0264142])
