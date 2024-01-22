#!/usr/bin/python3
"""This module defines a class named Rectangle that is inherited"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This defines a class Rectangle that is inherited"""
    def __init__(self, width, height):
        """Instantiation method"""
        integer_validator(width, 'width')
        integer_validator(height, 'height')
        self._width = width
        self._height = height
