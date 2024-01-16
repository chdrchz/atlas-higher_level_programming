#!/usr/bin/python3
"""This file contains a class defined as Rectangle"""


class Rectangle:
    """This is a class that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """This method initializes its properties"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
    """This method defines its width"""
        return self.__width

    @width.setter
    def width(self, value):
    """This method sets value to its width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
    """This method defines its height"""
        return self.__height

    @height.setter
    def height(self, value):
    """This method sets value to its height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
