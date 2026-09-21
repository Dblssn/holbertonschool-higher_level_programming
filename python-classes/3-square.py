#!/usr/bin/python3
""" Defines a class. """


class Square:
    """"This function defines a square.
    if size is not an int, it raises a TypeError.
    if size is less than 0, it raises a ValueError.
    It uses Public instance method: def area(self)
    that returns the current square area
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return (self.__size * self.__size)
