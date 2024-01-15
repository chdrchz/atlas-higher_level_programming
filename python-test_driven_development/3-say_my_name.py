#!/usr/bin/python3
"""This file defines a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """This function prints a name"""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        TypeError(
                "first_name must be a string or last_name must be a string"
        )
    print(f"My name is {first_name} {last_name}")
