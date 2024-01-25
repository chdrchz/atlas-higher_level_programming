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
    def size(self):
        """Size property"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method assigns attrs to args"""
        args_len = len(args)

        if args_len >= 1:
            self.id = args[0]
        if args_len >= 2:
            self.size = args[1]
        if args_len >= 3:
            self.x = args[2]
        if args_len >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
