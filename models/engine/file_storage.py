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
        with open(self.__file_path, 'w') as f:
            json.dump({
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
            }, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    objects = json.load(f)
                    for key, value in objects.items():
                        cls_name = value['__class__']
                        cls = all_classes.get(cls_name)
                        if cls:
                            FileStorage.__objects[key] = cls(**value)
            except json.JSONDecodeError:
                # Reset file content if it's invalid
                with open(self.__file_path, 'w') as f:
                    f.write('{}')
