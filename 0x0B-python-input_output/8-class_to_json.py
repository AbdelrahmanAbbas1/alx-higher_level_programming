#!/usr/bin/python3
"""This module defines a function"""


def class_to_json(obj):
    """This function returns the dictionary description with
        simple data structure

        Args:
            obj (obj): The object to be turned to JSON serialization

        Return:
            Returns the dictionary description
    """
    return obj.__dict__
