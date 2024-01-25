#!/usr/bin/python3
"""This module defines a class named Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This defines a class named Square inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """This method creates new instances of Square"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({id}) {}\{} - {}".format(
        self.id, self.x, self.y, self.size)