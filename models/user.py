#!/usr/bin/python3

""" Create a class user

Manage user functions
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
