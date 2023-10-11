#!/usr/bin/python3
"""This module contains BaseModel class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializing BaseModel class"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            date_time = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, date_time)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Define human readable of BaseModel Object"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates public instance updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Create a dict"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()

        return dict_obj

