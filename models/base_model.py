#!/usr/bin/env python3

from datetime import datetime


class BaseModel:
    """
    A base class for all models in this application.
    Attributes:
        id (str): The ID of the object.
        created_at (datetime): The time when the object was created.
        updated_at (datetime): The time when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel object.
        - If kwargs is passed, use it to set the object's attributes.
        - Otherwise, initialize with the current time and a generated ID.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __setattr__(self, key, value):
        """
        Custom __setattr__ to validate types for specific attributes.
        """
        if key in ['created_at', 'updated_at'] and not isinstance(value, datetime):
            raise TypeError(f"{key} must be a datetime object")
        super().__setattr__(key, value)

    def save(self):
        """
        Save the current object to the file storage (simulated).
        Updates the `updated_at` attribute.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat() \
            if isinstance(self.created_at, datetime) else self.created_at
        dict_rep['updated_at'] = self.updated_at.isoformat() \
            if isinstance(self.updated_at, datetime) else self.updated_at
        return dict_rep

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
