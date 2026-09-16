#!/usr/bin/python3

"""Define a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for x in row:
        if type(x) is not int and type(x) is not float:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                "matrix must have each row with the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
