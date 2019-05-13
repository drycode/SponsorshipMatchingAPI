"""LeagueSide interview API with endpoints for:
    Creating New Leagues in the database.
    Selecting the maximum number of leagues to sponsor within a budget.
The endpoints share the `/leagues` route.
"""

from flask import Flask, jsonify, request
from pymongo.errors import OperationFailure

from mongo.mongo_interface import add_league_to_db, get_leagues, verify_active_db

from data_models.league import _verify_coordinates
from error_handling.messages import (
    GET_VALUE_ERROR,
    GET_ATTRIBUTE_ERROR,
    POST_VALUE_ERROR,
    PYMONGO_OPERATION_ERROR,
)

APP = Flask(__name__)


@APP.route("/health")
def check_server():
    """Checks if the server is active."""
    return jsonify({"message": "Flask is up and running!"})


@APP.route("/database_health")
def check_database():
    """Checks if the database is active."""
    if not verify_active_db:
        return jsonify({"message": "The database has not been reached"})
    return jsonify({"message": "The database is active"})


@APP.route("/leagues", methods=["POST"])
def create_new_league():
    """Creates a new league in the database. Takes parameters `league_name`,
    `price`, and `coordinates`"""

    try:
        league_name, price, coordinates = _create_leagues_helper(request)

        if not league_name or not price or not coordinates:
            raise ValueError

        new_league = add_league_to_db(league_name, price, coordinates)

        return jsonify(repr(new_league)), 201

    except ValueError:
        return jsonify(POST_VALUE_ERROR), 400


@APP.route("/leagues", methods=["GET"])
def get_select_leagues():
    """Returns a list of leagues selected for sponsorship within a given budget, and
    within a specified radius of a location."""

    try:
        total_budget, search_radius, central_location = _get_leagues_helper(request)

        selected_leagues, remaining_budget = get_leagues(
            total_budget, search_radius, central_location
        )

        msg = {
            "leagues_to_sponsor": selected_leagues,
            "remaining_budget": remaining_budget,
        }

        return jsonify(msg), 200

    except AttributeError:
        return jsonify(GET_ATTRIBUTE_ERROR), 400

    except ValueError:
        return jsonify(GET_VALUE_ERROR), 400

    except OperationFailure:
        return jsonify(PYMONGO_OPERATION_ERROR), 400


def _create_leagues_helper(req):
    if req.json:
        league_name = req.json["league_name"]
        price = req.json["price"]
        coordinates = _verify_coordinates(req.json["coordinates"])

    else:
        league_name = req.args.get("league_name", type=str)
        price = req.args.get("price", type=int)
        coordinates = [
            int(x)
            for x in _verify_coordinates(
                req.args.get("coordinates", type=str).strip("[]").split(",")
            )
        ]

    return league_name, price, coordinates


def _get_leagues_helper(req):
    if req.json:
        total_budget = req.json["total_budget"]
        search_radius = req.json["search_radius"]
        central_location = req.json["central_location"]

    else:
        total_budget = req.args.get("total_budget", type=int)
        search_radius = req.args.get("search_radius", type=int)
        central_location = [
            int(x)
            for x in req.args.get("central_location", type=str).strip("[]").split(",")
        ]

    return total_budget, search_radius, central_location


if __name__ == "__main__":
    APP.config["DEBUG"] = True
    APP.run()
