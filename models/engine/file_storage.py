#!/usr/bin/python3
"""importing all necessary classes to be used"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""Defining a base class FileStorage"""


class FileStorage():
    """creating instances of class fileStorage
    that serializes instance to a json file and
    desrialise json file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dic = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """Method that deserializes the JSON file to __objects"""
        self.__classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "Place": Place,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for objs in obj_dict.values():
                    cls_name = objs["__class__"]
                    del objs["__class__"]
                    self.new(eval(f"{cls_name}")(**objs))
        except FileNotFoundError:
            pass

    def classes(self):
        """return dictionary rep of classes"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Return attributes and types"""
        return {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
