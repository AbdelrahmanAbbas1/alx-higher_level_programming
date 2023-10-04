#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle():
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a printable string"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for k in range(self.width):
                string += "#"
            if i != self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Returns a rpresentaion of a string"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
