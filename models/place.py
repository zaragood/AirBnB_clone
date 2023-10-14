#!/usr/bin/python3
"""This module contains Place class that inherit from BaseModel"""
from base_model import BaseModel


class Place(BaseModel):
    """Place Class attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    amenity_ids = []
