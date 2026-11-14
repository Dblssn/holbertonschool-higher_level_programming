#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student."""
        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for key, value in json.items():
            setattr(self, key, value)
