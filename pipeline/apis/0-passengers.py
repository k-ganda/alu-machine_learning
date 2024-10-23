#!/usr/bin/env python3
import requests
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
    url = 'https://swapi-api.alx-tools.com/api/starships/'
    ships = []
    while url:
        # Fetch data from the API
        response = requests.get(url)
        data = response.json()

        # Loop through each ship in the current page
        for ship in data['results']:
            # Check if the passenger field is known and a valid number
            passengers = ship['passengers']
            if passengers.isdigit():  # Some may be 'unknown'
                if int(passengers) >= passengerCount:
                    ships.append(ship['name'])

        # Move to the next page (if any)
        url = data['next']
    return ships
