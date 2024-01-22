#!/usr/bin/python3
"""This module defines a class named Rectangle, inherited"""


class Rectangle(BaseGeometry):
    """This defines a class Rectangle, inherited"""
    def __init__(self, width, height):
        """Instantiation method"""
        integer_validator(width, 'width')
        integer_validator(height, 'height')
        self._width = width
        self._height = height

    def integer_validator(value, name):
        """This defines a method that validates value, inherited"""
    if not isinstance(value, int) or value <= 0:
        raise ValueError("{} must be a positive integer".format(name))
