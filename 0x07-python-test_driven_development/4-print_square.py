#!/usr/bin/python3
"""Defines print_square function"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): The length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is float and less than 0
        ValueError: If size is not >=0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()
