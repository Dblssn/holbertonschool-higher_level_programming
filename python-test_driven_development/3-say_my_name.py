#!/usr/bin/python3
"""Define a function that prints  My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """ This function prints first name and last name
    If fist name is not a string a TypeError is raised
    If last name is not a string a TypeError is raised
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
