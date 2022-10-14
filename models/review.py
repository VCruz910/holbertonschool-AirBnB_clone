#!/usr/bin/python3
"""
Defines the users'
reviews.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews created by users
    about the place they stayed.
    """

    place_id = ""
    user_id = ""
    text = ""
