#!/usr/bin/python3
"""This module defines a Class"""


class Base():
    """This class represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the class

        Args:
            id (int): The id of the new instance

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
