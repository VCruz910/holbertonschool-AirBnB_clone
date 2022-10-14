#!/usr/bin/python3
"""
Defines places
for AirBnB.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Places for AirBnB.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []