#!/usr/bin/python3
"""Define a function that prints a text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """This function prints a text with 2 new lines
    after each of these char:., ? and:
    if the text is not a string a TypeError will be raised
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    print(text, end="")
