#!/usr/bin/python3
"""
This module defines the User class for AirBnB clone
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    Represents a user with basic info
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance
        """
        super().__init__(*args, **kwargs)

