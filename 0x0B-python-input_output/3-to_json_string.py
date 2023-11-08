#!/usr/bin/python3
"""This module defines a function"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object

        Args:
            my_obj (obj): The object to be serialized

        Return:
            The JSON representaion of an object (string)
    """
    return json.dumps(my_obj)
