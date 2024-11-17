#!/usr/bin/env python3
import json
import os
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """
    Handles saving and loading data from a JSON file.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the objects dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Save all objects to the file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Load all objects from the file if it exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    # Add other model types here if necessary
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
