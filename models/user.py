#!/usr/bin/python3
"""This module contains the User class that inherits
from the BaseModel class"""
from base import BaseModel


class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
