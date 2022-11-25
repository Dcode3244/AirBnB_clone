#!/usr/bin/python3
""" defines a User class that inherits from BaseModel class """
from models.base_model import BaseModel


class User(BaseModel):
    """ a class defining Users  """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
