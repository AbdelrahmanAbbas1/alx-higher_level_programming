#!/usr/bin/python3
"""This module defines a Class that inherits from another class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing a Rectangle"""
    def __init__(self, width, height):
        """Initializes a new rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String represents method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
