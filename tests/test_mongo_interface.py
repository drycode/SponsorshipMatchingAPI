from mongo.mongo_interface import (
    add_league_to_db,
    get_leagues,
    League,
    _compile_local_leagues,
)

from sample_data import leagues


class TestLeagueClass:
    def test__init__(self):
        x = League("The Mighty Ducks", 4300, [23.082395, -78.221348])
        assert x.asdict() == {
            "name": "The Mighty Ducks",
            "price": 4300,
            "coordinates": (23.082395, -78.221348),
        }
