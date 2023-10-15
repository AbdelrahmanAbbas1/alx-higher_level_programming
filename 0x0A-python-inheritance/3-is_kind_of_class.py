#!/usr/bin/python3
"""This module defines a function"""


def is_kind_of_class(obj, a_class):
    """This function checks the instance of the object

    Args:
        obj (obj): The object to be checked
        class (class): The class to be checked

    Return:
        True if the obj is an instance of the class
        or its subclass or false otherwise
    """
    return isinstance(obj, a_class)
