#!/usr/bin/python3
""" define function

this function adds 2 integers or floats
It returns an addition of a and b
"""
def add_integer(a, b=98):
    """ Add 2 integer
    
    """
    if type(a) is not (int) and type(a) is not (float):
        raise TypeError("a must be an integer")
    if type(b) is not (int) and type(b) is not (float):
        raise TypeError("b must be an integer")
    
    return int(a + b)
