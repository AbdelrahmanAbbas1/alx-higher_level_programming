#!/usr/bin/python3
"""This module defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
