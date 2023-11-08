#!/usr/bin/python3
"""This module defines a function"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file

        Args:
            filename (str): The name of the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
