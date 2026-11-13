#!/usr/bin/python3
"""Module converting a class to JSON"""


def class_to_json(obj):
    """Function returning dict of a class"""
    return obj.__dict__
