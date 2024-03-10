#!/usr/bin/python3

"""Implement Place

Implementation of class Place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place implementation"""

    city_id = ""  # will be City.id
    user_id = ""  # will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # will be a list of Amenity.id
