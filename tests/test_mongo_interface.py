"""Tests of the MongoDB interface for the LeagueSide sponsorship API"""

from pytest import mark, raises
import mongomock

from mongo.mongo_interface import (
    add_league_to_db,
    get_leagues,
    verify_active_db,
    _compile_local_leagues,
)

from sample_data import SAMPLE_LEAGUES, CENTRAL_LOCATION

MOCK_DB = mongomock.MongoClient().db
MOCK_COLLECTION = MOCK_DB.collection
MOCK_COLLECTION.insert_many(SAMPLE_LEAGUES)


@mark.parametrize(
    "search_radius, central_location, expected",
    {(5, CENTRAL_LOCATION, 6), (100, CENTRAL_LOCATION, 8), (0, CENTRAL_LOCATION, 0)},
)
def test__compile_local_leagues(search_radius, central_location, expected):
    """Tests collection of leagues within certain radius of the central location"""
    assert (
        len(_compile_local_leagues(search_radius, central_location, MOCK_COLLECTION))
        == expected
    )


@mark.parametrize(
    "total_budget, search_radius, central_location, expected",
    {
        (1000, 5, CENTRAL_LOCATION, (0, 1000)),
        (7800, 5, CENTRAL_LOCATION, (4, 410)),
        (3000, 5, (-41, 85), (0, 3000)),
        (7500, 16, (40, -73), (1, 4500)),
    },
)
def test_get_leagues(total_budget, search_radius, central_location, expected):
    """Tests collection of leagues within certain radius, and remaining budget after selected
    sponsorship"""
    selected_leagues, remaining_budget = get_leagues(
        total_budget, search_radius, central_location, MOCK_COLLECTION
    )
    assert (len(selected_leagues), remaining_budget) == expected


@mark.parametrize("total_budget, search_radius, central_location", {(None, None, None)})
def test_fail_get_leagues(total_budget, search_radius, central_location):
    """Tests that TypeError is raised when get_leagues is passed None Values"""
    with raises(TypeError):
        get_leagues(total_budget, search_radius, central_location, MOCK_COLLECTION)


def test_add_league_to_db():
    """Tests the addition of a new League to the mocked MongoDB database"""
    assert (
        str(
            add_league_to_db(
                "The Mighty Ducks", 2300, CENTRAL_LOCATION, MOCK_COLLECTION
            )
        )
        == "The Mighty Ducks -- Price: 2300, Coordinates(latitude=40.0274622857143, longitude=-75.0562142)"
    )


def test_verify_active_db():
    """Tests the method call to check if database is active"""
    assert verify_active_db(MOCK_COLLECTION, MOCK_DB)
