#!/usr/bin/python3
"""
This module defines a function that adds all arguments to a Python list
then saves them to a file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


file_name = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(fname)
except:
    pass

for f in range(1, len(sys.argv)):
    my_list.append(sys.argv[f])

save_to_json_file(my_list, file_name)
