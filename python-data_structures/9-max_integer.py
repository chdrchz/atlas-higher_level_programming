#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None
    max_number = sorted(my_list, reverse=True)[0]
