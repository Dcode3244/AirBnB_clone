#!/usr/bin/python3
""" defines all common attributes/methonds for other classes """

from datetime import datetime
import uuid
import models


class BaseModel():
    """ defines all common attributes/ methods for other classes """
    def __init__(self, *args, **kwargs):
        """ initializez BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(val)
                else:
                    if key != "__class__":
                        self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """ string representation of the BaseModel class """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ updated the public instance attribute updated_at with the current
        date and time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values if __dict__
        of the instance"""
        d = (self.__dict__).copy()
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = (self.updated_at).isoformat("T")
        d["created_at"] = (self.created_at).isoformat("T")
        return d
