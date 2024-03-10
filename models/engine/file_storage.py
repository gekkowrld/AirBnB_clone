#!/usr/bin/python3

"""Serialize and deserialize the data

The data is written from a file then subsequently written to a file
"""
import json
from getpass import getuser as gu
from os import path

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Store details and read details to JSON file"""

    def __init__(self):
        self.__file_path = FileStorage.__generate_filename()
        self.__objects = {}
        self.__cls = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
            "City": City,
            "State": State,
        }

    @staticmethod
    def __generate_filename():
        """Generate unique but permanent filename"""

        filename = "file"  # Default filename
        username = "username"

        # Try and get the username
        try:
            username = "".join(gu().split())  # Remove spaces
        except EnvironmentError:
            pass

        # Join the filename and username
        filename = f"{filename}_{username}"

        return f"{filename}.json"

    def all(self):
        """Return most of the objects"""

        return self.__objects

    def new(self, obj):
        """Set in __objects and obj with key <obj class name>.id"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Serialize __objects and then save then to __file_path"""

        # Prepare the data first
        __pd = {}

        for key, val in self.__objects.items():
            __pd[key] = val.to_dict()

        # Write the data to file
        with open(self.__file_path, "w", encoding="UTF-8") as fo:
            fo.write(json.dumps(__pd))

    def reload(self):
        """Open the __file_path for reading

        After reading, load __objects with the information
        Only do so if the file exists, else do nothing
        """

        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="UTF-8") as fr:
                    fc = json.loads(fr.read())
                    for key, val in fc.items():
                        obj = self.__cls[val["__class__"]](**val)
                        self.__objects[key] = obj
            except json.JSONDecodeError:
                pass
