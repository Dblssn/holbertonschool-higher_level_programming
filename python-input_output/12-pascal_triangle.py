#!/usr/bin/python3
"""Pascal's Triangle hat returns a list of lists of integers"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle."""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                number = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(number)

            row.append(1)

        triangle.append(row)

    return triangle
