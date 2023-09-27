#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): The size of the new Square
            position (tuple): The position of the new Square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns: The size of the new Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the new Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            for i in value:
                if i >= 0:
                    continue
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return self.__size**2

    def my_print(self):
        """Prints the new Square with #"""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
