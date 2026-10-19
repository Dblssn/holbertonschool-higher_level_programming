#!/usr/bin/python3
"""Define this function
"""


def read_file(filename=""):
    """This function that reads a text file

    """

    with open(filename, "r",  encoding="utf-8") as f:
        print(f.read(), end="")
