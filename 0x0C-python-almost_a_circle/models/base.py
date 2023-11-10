#!/usr/bin/python3
"""This module defines a Base class"""
import json


class Base():
    """This class represents a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function assign id with a certain value

            Args:
                id (int): The id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation pf list_dictionaries"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"
