#!/usr/bin/python3
"""This module defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file

        Args:
            my_obj (obj):
    """
    with open(filename, "a", encoding="utf-8") as f:
        json.dump(my_obj, f)
