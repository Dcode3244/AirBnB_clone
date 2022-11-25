#!/usr/bin/python3
""" defines a Citye class that inherits from BaseModel class """
from models.base_model import BaseModel


class City(BaseModel):
    """ a class defining City  """

    name = ""
    state_id = ""
