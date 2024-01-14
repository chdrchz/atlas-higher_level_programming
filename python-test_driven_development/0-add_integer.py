#!/usr/bin/python3
"""This module defines a function that adds two integers"""

def add_integer(a, b=98):
    """This function adds two integers and returns the result"""
    if not isinstance(a, int) or not isinstance(b, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(a, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
