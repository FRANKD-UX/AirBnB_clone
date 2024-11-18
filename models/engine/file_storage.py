#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __classes = {"State": State, "City": City,
                 "Amenity": Amenity, "Place": Place, "Review": Review}

    def all(self):
        """Returns the dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves all objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Reloads all objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name in self.__classes:
                        FileStorage.
                        __objects[key] = self.__classes[class_name](
                            **value)
        except FileNotFoundError:
            pass  # If the file doesn't exist, no data is loaded
