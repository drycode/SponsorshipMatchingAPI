"""Sample data for tests"""
from data_models.league import Coordinates

CENTRAL_LOCATION = Coordinates(40.0274622857143, -75.0562142)

T1 = Coordinates(40.0274622857143, -77.0562142)
T2 = Coordinates(40.0274622851143, -75.0552142)
T3 = Coordinates(40.0274622852143, -75.0564142)
T4 = Coordinates(40.0274622852143, -75.2561421)
T5 = Coordinates(40.0276623852143, -75.0164142)
T6 = Coordinates(40.0274622857143, -77.0563142)
T7 = Coordinates(40.0274622851143, -75.0552142)
T8 = Coordinates(40.0274622852143, -75.0564142)
T9 = Coordinates(40.0274622852143, -75.2461421)
T10 = Coordinates(40.0276623852143, -75.0264142)
T11 = Coordinates(40, -73)

SAMPLE_LEAGUES = [
    {"name": "The Wyld Stallions", "price": 4500, "coordinates": T1},
    {"name": "Team Zoidberg", "price": 6000, "coordinates": T2},
    {"name": "The Zoomers", "price": 1500, "coordinates": T3},
    {"name": "North Horseburg Little League", "price": 3500, "coordinates": T4},
    {"name": "The Duloc Ogres", "price": 2500, "coordinates": T5},
    {"name": "Team 6", "price": 3550, "coordinates": T6},
    {"name": "Team 7", "price": 2130, "coordinates": T7},
    {"name": "Team 8", "price": 1620, "coordinates": T8},
    {"name": "Team 9", "price": 2700, "coordinates": T9},
    {"name": "Team 10", "price": 2140, "coordinates": T10},
    {"name": "Team 11", "price": 3000, "coordinates": T11},
]
