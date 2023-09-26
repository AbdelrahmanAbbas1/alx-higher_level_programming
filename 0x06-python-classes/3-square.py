#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initializes a new Square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns The area of the new square"""
        return self.__size**2
