#!/usr/bin/python3
"""
This module defines the BaseModel class for AirBnB clone
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all AirBnB clone models
    Handles id, creation, update, serialization
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        If kwargs is provided, creates instance from dictionary.
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, fmt))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with current datetime and saves instance
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

