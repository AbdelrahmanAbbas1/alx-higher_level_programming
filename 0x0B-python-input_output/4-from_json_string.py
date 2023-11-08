#!/usr/bin/python3
"""This module defines a function"""
import json


def from_json_string(my_str):
    """This function returns an object by a json string

        Args:
            my_str (str): The string to be converted to object

        Return:
            An object represented by a JSON string
    """
    return json.loads(my_str)
