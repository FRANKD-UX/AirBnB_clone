#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes and deserializes objects to and from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage objects to the JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict()
                      for k, v in self.__objects.items()}, f)

    def reload(self):
        """Loads storage objects from the JSON file."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name in self.__classes:
                    self.__objects[key] = self.__classes[class_name](
                        **value)
        except FileNotFoundError:
            pass
