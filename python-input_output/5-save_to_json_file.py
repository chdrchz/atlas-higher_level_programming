#!/usr/bin/python3
"""
This module defines a function that writes an object to a text file
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file using JSON rep"""
    json_obj = json.dumps(my_obj)
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(json_obj)
