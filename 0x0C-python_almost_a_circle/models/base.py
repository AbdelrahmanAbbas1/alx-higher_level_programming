#!/usr/bin/python3
"""This module defines a Base class"""


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
