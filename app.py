"""LeagueSide interview API with endpoints for:
    Creating New Leagues in the database.
    Selecting the maximum number of leagues to sponsor within a budget.
The endpoints share the `/leagues` route.
"""

from flask import Flask, jsonify, request
from mongo.mongo_interface import add_league_to_db, get_leagues, verify_active_db


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
    if not request.json:
        msg = {"msg": "Request body must include league_name, price, and coordinates"}
        return jsonify(msg), 400

    try:
        new_league = add_league_to_db(
            request.json["league_name"],
            request.json["price"],
            request.json["coordinates"],
        )
        print(new_league)
        return jsonify(repr(new_league)), 201

    except Exception as err:
        print(f"Invalid input returned from client: {request.json}")
        return err, 400


@APP.route("/leagues", methods=["GET"])
def get_select_leagues():
    """Returns a list of leagues selected for sponsorship within a given budget, and
    within a specified radius of a location."""
    if not request.json:
        msg = {
            "msg": "Request body must include total_budget, search_radius, and central_location"
        }
        return jsonify(msg), 400

    try:
        selected_leagues, remaining_budget = get_leagues(
            request.json["total_budget"],
            request.json["search_radius"],
            request.json["central_location"],
        )
        print(selected_leagues, remaining_budget)
        # order response by name, price, coordinates
        msg = {
            "leagues_to_sponsor": selected_leagues,
            "remaining_budget": remaining_budget,
        }
        return jsonify(msg), 200

    except Exception as err:
        print(f"Invalid input returned from client: {request.json}")
        return err, 404


if __name__ == "__main__":
    APP.run()
