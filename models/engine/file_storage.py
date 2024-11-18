#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class to manage serialization and deserialization of objects"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to the __objects dictionary"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects to the file"""
        with open(FileStorage.__file_path, 'w') as f:
            objs = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
            json.dump(objs, f)

    def reload(self):
        """Reloads objects from the file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for key, obj_data in objs.items():
                    class_name = obj_data["__class__"]
                    class_ = globals().get(class_name)
                    if class_:
                        FileStorage.__objects[key] = class_(**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the __objects dictionary"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
