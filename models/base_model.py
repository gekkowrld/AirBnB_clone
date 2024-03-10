#!/usr/bin/python3

""" A class that acts as the base for other classes

The class has the following instances by default:
    - id: uses uuid.uuid4() to generate the uuid.
        The value however is returned as a string

    - created_at: The datetime that the current instance is
        created at.

    - updated_at: Originally contain the value of `created_at`
        but then update as the instance is being updated.
        This means overwrite the previous values
"""

from datetime import datetime
from uuid import uuid4 as uid


class BaseModel:
    """Base Model

    Define the methods and objects that al the other
                                    classes will inherit
    """

    DATE_FMT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        from models import storage

        if kwargs:
            for key, val in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    setattr(
                        self, key, datetime.strptime(val, BaseModel.DATE_FMT)
                    )
                elif key != "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uid())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """Update the time"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Change how __str__ method behaves"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Convert to dict"""

        dict_obj = {}

        for obj_key, obj_val in self.__dict__.items():
            # Change the time to a 'str' in a special way
            if obj_key in {"updated_at", "created_at"}:
                dict_obj[obj_key] = obj_val.isoformat()
            else:
                dict_obj[obj_key] = obj_val

        dict_obj["__class__"] = self.__class__.__name__

        return dict_obj
