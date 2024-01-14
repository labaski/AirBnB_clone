#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class wzqPlace(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    wqzcity_id = ""
    wzquser_id = ""
    name = ""
    wzqdescription = ""
    wzqnumber_rooms = 0
    wzqnumber_bathrooms = 0
    wzqmax_guest = 0
    wzqprice_by_night = 0
    wzqlatitude = 0.0
    wzqlongitude = 0.0
    wzqamenity_ids = []
