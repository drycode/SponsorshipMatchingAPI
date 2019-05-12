"""Tests methods related to data models used by the API"""
from pytest import mark, raises
from data_models.league import League, _verify_coordinates


def test_asdict():
    """Tests dictionary representation of League instances"""
    league = League("The Mighty Ducks", 4300, [23.082395, -78.221348])
    assert league.asdict() == {
        "name": "The Mighty Ducks",
        "price": 4300,
        "coordinates": (23.082395, -78.221348),
    }


@mark.parametrize(
    "user_input, expected",
    {
        (
            League("The Mighty Ducks", 4300, [23.082395, -78.221348]),
            "The Mighty Ducks -- Price: 4300, Coordinates(latitude=23.082395, longitude=-78.221348)",
        ),
        (
            League("The Bruins", 3450, [84.2340958, -23.0923485]),
            "The Bruins -- Price: 3450, Coordinates(latitude=84.2340958, longitude=-23.0923485)",
        ),
    },
)
def test__repr__(user_input, expected):
    """Checks __repr__ special method of League instance"""
    assert repr(user_input) == expected


def test_empty_league():
    """Checks against None/empty parameters for League instance"""
    with raises(TypeError):
        League(None, None, [])


@mark.parametrize("input", {(-90, 0), (90, 91), (23, 180), (-1, -180)})
def test__verify_coords(input):
    """Checks verify coordinates function"""
    assert _verify_coordinates(input) == input


@mark.parametrize("input", {(-2344, 90), (91, 91), (-1, 181), (-1, -190)})
def test__fail_verify_coords(input):
    """Checks verify coordinates function"""
    with raises(ValueError):
        _verify_coordinates(input)
