#!/usr/bin/python3
"""This module defines a function"""


def inherits_from(obj, a_class):
    """This function checks the instance of the object

    Args:
        obj (obj): The object to be checked
        class (class): The class to be checked

    Return:
        True if the obj is an instance of a class that is
        inherited directly or indirectly from the specified class
        or false otherwise
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    else:
        return False
