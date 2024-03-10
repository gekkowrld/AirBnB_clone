#!/usr/bin/python3

"""Review

Implement review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Implement review"""

    place_id = "" # Will be Review.id
    user_id = "" # will be User.id
    text = ""
