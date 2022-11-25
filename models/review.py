#!/usr/bin/python3
""" defines a Review class that inherits from BaseModel class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ a class defining Review """

    place_id = ""
    user_id = ""
    text = ""
