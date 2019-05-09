from collections import namedtuple

coordinates = namedtuple("Coordinates", "latitude longitude")

central_location = coordinates(40.0274622857143, -75.0562142)
t1 = coordinates(40.0274622857143, -77.0562142)
t2 = coordinates(40.0274622851143, -75.0552142)
t3 = coordinates(40.0274622852143, -75.0564142)
t4 = coordinates(40.0274622852143, -75.2561421)
t5 = coordinates(40.0276623852143, -75.0164142)
t6 = coordinates(40.0274622857143, -77.0563142)
t7 = coordinates(40.0274622851143, -75.0552142)
t8 = coordinates(40.0274622852143, -75.0564142)
t9 = coordinates(40.0274622852143, -75.2461421)
t10 = coordinates(40.0276623852143, -75.0264142)

leagues = [
    {"name": "The Wyld Stallions", "price": 4500, "location": t1},
    {"name": "Team Zoidberg", "price": 6000, "location": t2},
    {"name": "The Zoomers", "price": 1500, "location": t3},
    {"name": "North Horseburg Little League", "price": 3500, "location": t4},
    {"name": "The Duloc Ogres", "price": 2500, "location": t5},
    {"name": "Team 6", "price": 3550, "location": t6},
    {"name": "Team 7", "price": 2130, "location": t7},
    {"name": "Team 8", "price": 1620, "location": t8},
    {"name": "Team 9", "price": 2700, "location": t9},
    {"name": "Team 10", "price": 2140, "location": t10},
]
