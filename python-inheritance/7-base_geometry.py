#!/usr/bin/python3
"""This module defines a class named BaseGeometry"""


class BaseGeometry:
    """This defines a class named BaseGeometry"""
    def area(self):
        """public instance method that calculates area"""
        raise Exception("area() is not defined")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be greater than 0")
