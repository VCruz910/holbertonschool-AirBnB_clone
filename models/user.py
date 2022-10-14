#!/usr/bin/python3
"""
Creates the user.
"""

from models.base_model import BaseModel


class User(BaseModel):
        """
        Defines the user's
        attributes for creation.
        """

        email = ""
        password = ""
        first_name = ""
        last_name = ""
