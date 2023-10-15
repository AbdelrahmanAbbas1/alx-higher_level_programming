#!/usr/bin/python3
"""This module defines a function"""


def is_same_class(obj, a_class):
    """Checks the instanceof the class

    Args:
        obj (obj): An instance of the class
        class (class): The class

    Return:
        True if the obj is an instance and false otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
