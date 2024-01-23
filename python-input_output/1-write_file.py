#!/usr/bin/python3
"""This module defines a function that appends to a file"""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a text file
    and returns the number of new characters added
    """
    new_chars = 0
    with open(filename, encoding="utf-8") as file:
        file.write(text)
        new_chars = len(text)
        return(new_chars)
