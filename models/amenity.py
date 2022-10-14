#!/usr/bin/python3
"""
Defines the amenities
of the client.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the amenities that
    the user can choose from to
    offer at its place.
    """
    name = ""
