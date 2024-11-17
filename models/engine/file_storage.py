#!/usr/bin/python3
"""FileStorage class for storing and retrieving objects"""
import json
from models.base_model import BaseModel
from models.user import User  # Import User class


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    # Updated dictionary with User class
    __classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name in self.__classes:
                    self.__objects[key] = self.__classes[class_name](**value)
        except FileNotFoundError:
            pass
