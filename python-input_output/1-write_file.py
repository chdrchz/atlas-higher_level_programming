#!/usr/bin/python3
"""This module defines a function that writes to a file"""


    def write_file(filename="", text=""):
    """
    This function writes to a file and returns the number of new chars
    """
    new_chars = 0
    with open(filename, encoding="utf-8") as file:
        file.write(text)
        new_chars = len(text)
        return(new_chars)
