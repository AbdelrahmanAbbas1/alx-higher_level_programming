#!/usr/bin/python3
"""This Module defines a class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A subclass representing a Square"""
    def __init__(self, size):
        """Initializes a new square

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Stirng representation method"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
