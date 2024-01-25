#!/usr/bin/python3
"""This module defines a class named Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This defines a class named Square inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """This method creates new instances of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def width(self):
        return self.size
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
    
    @property
    def height(self):
        return self.size
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.height = value
