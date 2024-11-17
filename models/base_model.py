#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models in this project.
    Handles id and datetime management.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments for custom initialization.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())  # Generates a unique ID
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)  # Add instance to storage

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}"
        .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
