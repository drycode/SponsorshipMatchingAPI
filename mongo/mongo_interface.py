"""This file provides methods used by to access the MongoDB database by the Flask
Application. """

from pymongo.errors import OperationFailure
from mongo.mongo_config import DB, LEAGUES_COLLECTION as L_COL

from data_models.league import League

EQUATORIAL_RADIUS = 3963.2


def get_leagues(total_budget, search_radius, central_location, collection=L_COL):
    """Returns a list of leagues to sponsor within a given budget and location"""
    local_leagues = _compile_local_leagues(search_radius, central_location, collection)
    local_leagues.sort(key=lambda x: x["price"])

    selected_leagues = []

    remaining_budget = total_budget

    for league in local_leagues:
        total_budget -= league["price"]

        # If league is within remaining budget, add to list, and update current remaining_budget
        if total_budget >= 0:
            remaining_budget = total_budget
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

    new_league = League(league_name, price, coordinates)

    if existing:
        collection.update_one({"_id": existing["_id"]}, {"$set": new_league.asdict()})
    else:
        collection.insert_one(new_league.asdict())

    return new_league


def verify_active_db(collection=L_COL, database=DB):
    """Checks the existence/accessibility of the MongoDB instance"""
    try:
        return collection.name in database.list_collection_names()
    except OperationFailure:
        return False


def _compile_local_leagues(search_radius, central_location, collection):
    """Returns a list of leagues that fit within the given location parameters"""
    # Query parameters search radial distance from a central point
    # search_radius / EQUATORIAL_RADIUS returns radian
    query = {
        "coordinates": {
            "$geoWithin": {
                "$centerSphere": [
                    list(central_location),
                    search_radius / EQUATORIAL_RADIUS,
                ]
            }
        }
    }

    local_leagues = [x for x in collection.find(query)]

    return local_leagues
