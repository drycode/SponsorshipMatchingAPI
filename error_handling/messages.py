"""Module containing static error messages for the flask application"""

GET_VALUE_ERROR = {
    "msg": "Request body must include total_budget, search_radius, and central_location.",
    "required_parameters": {
        "total_budget": "Type(int)",
        "search_radius": "Type(int)",
        "central_location": "Type(list)",
    },
    "error": "ValueError: Make sure to use appropriate types in your request",
}


GET_ATTRIBUTE_ERROR = {
    "msg": "Request body must include total_budget, search_radius, and central_location.",
    "required_parameters": {
        "total_budget": "Type(int)",
        "search_radius": "Type(int)",
        "central_location": "Type(list)",
    },
    "error": "AttributeError: The API did not recieve a request",
}

POST_VALUE_ERROR = {
    "msg": "Request body must include league_name, price, and coordinates",
    "required_parameters": {
        "league_name": "Type(str)",
        "price": "Type(int)",
        "coordinates": "Type(list)",
    },
    "error": "ValueError: Make sure to use appropriate types in your request",
}

PYMONGO_OPERATION_ERROR = {
    "msg": "Coordinates must be valid in form lon/lat",
    "required_parameters": {
        "league_name": "Type(str)",
        "price": "Type(int)",
        "coordinates": {
            "type": "[longitude, latitude]",
            "longitude": "-180 to 180",
            "latitude": "-90 to 90",
        },
    },
    "error": "OperationError: Make sure coordinate values are valid values",
}

