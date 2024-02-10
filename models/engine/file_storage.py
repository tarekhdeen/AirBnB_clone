#!/usr/bin/python3
"""Module for JSON file"""
import json
import os
import datetime


class FileStorage:

    """A class serializes instances to a JSON file and deserializes them"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fl_pa:
                obj_dict = json.load(fl_pa)
                obj_dict = {key: self.classes()[value["__class__"]](**value)
                            for key, value in obj_dict.items()}
                FileStorage.__objects = obj_dict
        else:
            return

    def classes(self):
        """Class to manage serialization and deserialization of all"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        return {"BaseModel": BaseModel, "User": User, "Place": Place,
                "State": State, "City": City, "Amenity": Amenity,
                "Review": Review}

    def attributes(self):
        """Class converts the object's attributes to a dictionary"""

        return {"BaseModel": {"id": str, "created_at": datetime.datetime,
                              "updated_at": datetime.datetime},
                "User": {"email": str, "password": str,
                         "first_name": str, "last_name": str},
                "Place": {"city_id": str, "user_id": str, "name": str,
                          "description": str, "number_rooms": int,
                          "number_bathrooms": int, "max_guest": int,
                          "price_by_night": int, "latitude": float,
                          "longitude": float, "amenity_ids": list},
                "State": {"name": str},
                "City": {"state_id": str, "name": str},
                "Amenity": {"name": str},
                "Review": {"place_id": str, "user_id": str, "text": str}
                }
