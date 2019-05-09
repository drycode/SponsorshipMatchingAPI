# from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from test_data import leagues, central_location

# geolocator = Nominatim(user_agent="interface_layer")


def get_leagues(total_budget, search_radius, central_location):
    # Dynamic programming solution to the knapsack problem
    local_leagues = _compile_local_leagues(search_radius, central_location)
    return local_leagues


def _compile_local_leagues(search_radius, central_location):
    local_leagues = []
    for league in leagues:
        if geodesic(central_location, league["location"]).miles <= search_radius:
            local_leagues.append(league)
    return local_leagues


get_leagues(0, 5, central_location)
