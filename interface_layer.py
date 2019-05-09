# from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from test_data import leagues, central_location

# geolocator = Nominatim(user_agent="interface_layer")
total_budget = 7300


def get_leagues(total_budget, search_radius, central_location):
    """Returns a list of leagues to sponsor within a given budget and location"""
    local_leagues = _compile_local_leagues(search_radius, central_location)
    local_leagues.sort(key=lambda x: x["price"])

    selected_leagues = []
    for league in local_leagues:
        remaining_budget = total_budget
        total_budget -= league["price"]
        if total_budget >= 0:
            selected_leagues.append(league)
        else:
            break
    return selected_leagues, remaining_budget


def _compile_local_leagues(search_radius, central_location):
    """Returns a list of leagues that fit within the given location parameters"""
    local_leagues = []
    for league in leagues:

        # Checks the distance of the league's coordinates against the given location
        # If within the given search radius, the league is appended to the returned list
        if geodesic(central_location, league["location"]).miles <= search_radius:
            local_leagues.append(league)
    return local_leagues


selected_leagues, remaining_budget = get_leagues(total_budget, 5, central_location)
[print(league["name"]) for league in selected_leagues]
print(remaining_budget)
