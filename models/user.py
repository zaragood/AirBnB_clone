#!/usr/bin/python3
"""This module contains the User class that inherits
from the BaseModel class"""
from base_model import BaseModel


class User(BaseModel):
    """The user class inherits from BaseModel class"""
    def __init__(self):
        """initializing the user class"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
