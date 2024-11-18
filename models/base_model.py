#!/usr/bin/python3

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __setattr__(self, name, value):
        """Ensure 'created_at' and 'updated_at' attributes are datetime objects"""
        if name == "created_at" or name == "updated_at":
            if not isinstance(value, datetime):
                raise TypeError(f"{name} must be a datetime object")
        super().__setattr__(name, value)
