#!/usr/bin/python3
""" defines a class that sterializes instances to a JSON file
and deserializes JSON file to instances """
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ serializes and deserializes JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        objName = obj.__class__.__name__
        objKey = objName + "." + obj.id
        FileStorage.__objects[objKey] = obj

    def save(self):
        """ serializes __objects to the JSON file (parh: __file_path) """
        objs = FileStorage.__objects
        objD = {key: val.to_dict() for key, val in objs.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objD, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objD = json.load(f)
                for val in objD.values():
                    cName = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cName)(**val))
