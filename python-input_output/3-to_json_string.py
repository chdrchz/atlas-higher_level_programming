#!/usr/bin/python3
"""
This module defines a function that returns the json representation of a string
"""
import json


def to_json_string(my_obj):
    """This function returns the json representation of a string"""
    json_object = json.loads(my_obj)
    return my_obj
