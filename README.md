# LeagueSide Sponsorship API

> This project features my solution to the LeagueSide Interview Project.

![coverage][coverage]
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Project Requirements
#### ADD A LEAGUE TO THE SYSTEM
For the purposes of this exercise, a League is a collection of, at the very least:

1. A league name.
2. A latitude/longitude pair.
3. A single price to purchase their sponsorship opportunity.

#### FIND LEAGUES TO SPONSOR
This endpoint should accept a few arguments:

1. A latitude/longitude pair around which to focus the search.
2. A radius in miles in which to search around that central point.
3. A total budget to spend on leagues.


## Running development server
```sh
$ pip install -r requirements.txt
$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## API Endpoints

## GET
_-- Returns enough leagues to spend up to the budget, sponsoring as many leagues as possible without going over it. Also returns the remaining budget._
<br>
`/leagues`

#### Parameters

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `total_budget` | required | number  | The total amount to invest in sponsorship.                                                         |
|     `search_radius` | required | number  | The total distance in miles form the central location with which to query leagues.     
|     `central_location` | required | list  | The geographical position that the query will be initialized at, denoted as latitude and longitude in the form of `[lat, lon]`    |<br>

#### Example Response
```{
    "leagues_to_sponsor": [
        {
            "coordinates": [
                40.0276523242143,
                -75.0132142
            ],
            "name": "The Fighting Irish",
            "price": 1300
        },
        {
            "coordinates": [
                40.0274622852143,
                -75.0564142
            ],
            "name": "The Zoomers",
            "price": 1500
        },
    ],
    "remaining_budget": 950
}
```

## POST
_-- Adds a new league to the database._ 

<br>

`/leagues`
|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `league_name` | required | number  | The name of the new league.                                                                     |
|     `price` | required | number  | The cost required to sponsor the league.     
|     `coordinates` | required | list  | The geographical position that the league is located, denoted as latitude and longitude in the form of `[lat, lon]`    

#### Example Response
```
"The Red Sox -- Price: 2400, Coordinates(latitude=40.03423242143, longitude=-75.13485)"
```



[coverage]: ./coverage.svg
