#!/usr/bin/python3
"""This module defines a function that adds two integers"""

def add_integer(a, b=98):
    """This function adds two integers and returns the result"""

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        return float(a + b)
    return int(a + b)
