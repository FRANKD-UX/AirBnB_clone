#!/usr/bin/env python3
"""
Handles the storage of objects in a JSON file.
"""

import json
import os
from models.base_model import BaseModel

# Mapping of class names to their respective classes
all_classes = {
    "BaseModel": BaseModel,
    # Add other model classes here, e.g., "User": User, "Place": Place
}


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to __objects dictionary.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
            }, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if it exists and is valid).
        """
        if os.path.exists(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 0:
                try:
                    with open(FileStorage.__file_path, 'r') as f:
                        objects = json.load(f)
                        for key, value in objects.items():
                            cls_name = value['__class__']
                            cls = all_classes.get(cls_name)
                            if cls:
                                FileStorage.__objects[key] = cls(**value)
                except json.JSONDecodeError:
                    print(
                        f"Warning: Failed to decode {FileStorage.__file_path}. "
                        "The file might be corrupted or invalid."
                    )
