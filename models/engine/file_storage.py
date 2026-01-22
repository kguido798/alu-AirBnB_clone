#!/usr/bin/python3
"""
This module defines the FileStorage class
for serialization and deserialization of instances
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to __objects dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**val)
                    elif cls_name == "User":
                        self.__objects[key] = User(**val)
        except FileNotFoundError:
            pass

