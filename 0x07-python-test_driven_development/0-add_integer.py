#!/usr/bin/python3
""" 0-add_integer.py """


def add_integer(a, b=98):
    """Adds two integers

    Args:
    a (int): The first number
    b (int): The seconde number

    Raises:
    TypeError: if either a or b in non integer of non float

    Returns: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
