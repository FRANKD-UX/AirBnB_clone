#!/usr/bin/env python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        # If kwargs is provided, initialize from it
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.updated_at = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
            self.created_at = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
        else:
            # If no kwargs, create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Save the instance to storage"""
        from models import storage  # Import storage inside
        # the method to avoid circular import
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }
