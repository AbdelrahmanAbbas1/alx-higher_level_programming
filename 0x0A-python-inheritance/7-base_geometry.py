#!/usr/bin/python3
"""This module defines a Class"""


class BaseGeometry():
    """This Class represents BaseGeometry"""
    def area(self):
        """This function raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
