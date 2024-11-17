#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage  # Import the storage instance


class BaseModel:
    """Base class for all models in the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs:
            # If a dictionary is provided, initialize the object from it
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = datetime.fromisoformat(kwargs.get('created_at'))
            self.updated_at = datetime.fromisoformat(kwargs.get('updated_at'))
        else:
            # Otherwise, create a new instance with a unique ID and timestamps
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  # Add the object to the storage

    def __str__(self):
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current
        datetime and save to storage."""
        self.updated_at = datetime.now()
        storage.save()  # Call save on storage to persist the objects

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
