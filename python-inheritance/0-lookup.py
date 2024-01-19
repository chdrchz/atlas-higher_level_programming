#!/usr/bin/python3
"""This module defines a function that returns a list"""


def lookup(obj):
    """This function returns a list"""
    methods_attributes = dir(obj)
    return methods_attributes
