#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back"""

    __file_path = "file.json"
    __objects = {}

    __classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump(
                {key: obj.to_dict()
                 for key, obj in self.__objects.items()}, f
            )

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.pop("__class__", None)
                    if class_name in self.__classes:
                        self.__objects[key] = self.__classes[class_name](
                            **value)
        except FileNotFoundError:
            pass
