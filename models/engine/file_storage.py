#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Handles storage of objects in JSON format."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves the current objects to the file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Reloads objects from the file."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
