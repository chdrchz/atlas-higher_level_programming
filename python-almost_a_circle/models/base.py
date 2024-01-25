#!/usr/bin/python3
"""This module defines a class named base"""


class Base:
    """This is a class named Base"""
    def __init__(self, id=None):
        """This method is the class constructor"""
        __nb_objects = 0
        if id is not None:
            self.id = id
        __nb_objects += 1
        self.id = __nb_objects     