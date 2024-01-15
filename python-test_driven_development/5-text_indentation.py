#!/usr/bin/python3
"""This file defines a function that prints after characters"""


def text_indentation(text):
    """This function prints after special characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines = text.split()
    for line in lines:
        print(line.strip())
