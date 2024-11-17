#!/usr/bin/python3
"""
FileStorage module for serializing and deserializing objects
"""
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file at __file_path
        """
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict()
                      for k, v in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if it exists
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
