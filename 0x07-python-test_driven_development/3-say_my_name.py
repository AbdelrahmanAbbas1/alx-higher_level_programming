#!/usr/bin/python3
"""Defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints The full name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If the first_name is not a str
        TypeError: If the last_name is not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
