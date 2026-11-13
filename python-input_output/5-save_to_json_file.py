#!/usr/bin/python3
"""Saving object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to a JSON'ed text file"""

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
        