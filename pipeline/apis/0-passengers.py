#!/usr/bin/env python3
"""
Module containin a function
to return list of ships
"""


def availableShips(passengerCount):
    """
    Returns list of ships that
    can hold a given no of passengers
    if no ship available
    return empty list
    """
    import requests
    url = 'https://swapi-api.alx-tools.com/api/starships/'
    response = requests.get(url)
    data = response.json()
    ships = []

    for result in data['results']:
        if result['passengers'] != "n/a":
            passengers_no = int(result['passengers'].replace(',', ''))
            # print(passengers_no)
            if passengers_no >= passengerCount:
                ships.append(result['name'])

    return ships
