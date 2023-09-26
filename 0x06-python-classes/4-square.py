#!/usr/bin/python3
"""
3-square.py
Define a Square
"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get the size fo the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the new square"""
        return self.__size**2
