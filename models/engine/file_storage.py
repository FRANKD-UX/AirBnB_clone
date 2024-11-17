#!/usr/bin/env python3
import json
import os


class FileStorage:
    """
    Handles storage of objects to a JSON file.
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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the current objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Reloads objects from the JSON file.
        """
        try:
            if os.path.exists(FileStorage.__file_path)
            and os.stat(FileStorage.__file_path).st_size != 0:
                with open(FileStorage.__file_path, 'r') as f:
                    FileStorage.__objects = json.load(f)
        except json.JSONDecodeError:
            FileStorage.__objects = {}
