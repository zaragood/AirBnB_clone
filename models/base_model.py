#!/usr/bin/python3
"""This module contains BaseModel class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        """initializing BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

