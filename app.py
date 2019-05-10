from mongo.mongo_interface import add_league_to_db, get_leagues
from mongo.mongo_config import db


from flask import (
    Flask,
    jsonify,
    abort,
    make_response,
    request,
    session,
    url_for,
    redirect,
    Response,
)

app = Flask(__name__)


@app.route("/health")
def check_server():
    return jsonify({"message": "Flask is up and running!"})


@app.route("/database_health")
def check_database():
    pass


@app.route("/leagues", methods=["POST"])
def create_new_league():
    if not request.json:
        msg = {"msg": "Request body must include league_name, price, and coordinates"}
        return jsonify(msg), 400

    else:
        try:
            new_league = add_league_to_db(
                request.json["league_name"],
                request.json["price"],
                request.json["coordinates"],
            )
            print(new_league)
            return jsonify(repr(new_league)), 201

        except Exception as e:
            print(f"Invalid input returned from client: {request.json}")
            return e, 400


@app.route("/leagues", methods=["GET"])
def get_select_leagues():
    if not request.json:
        msg = {
            "msg": "Request body must include total_budget, search_radius, and central_location"
        }
        return jsonify(msg), 400

    else:
        # try:
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

        # except Exception as e:
        #     print(f"Invalid input returned from client: {request.json}")
        #     return e, 404


if __name__ == "__main__":
    app.run()
