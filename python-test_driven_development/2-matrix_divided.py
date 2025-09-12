#!/usr/bin/python3
"""Defines function to scalar divide a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a scalar.

    Args:
        matrix (list of lists): matrix with int/float elements
        div (int/float): divisor (must not be 0)

    Returns:
        list of lists: new matrix with elements divided by div,
        rounded to 2 decimal places
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(error_msg)

    if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
               for row in matrix for x in row):
        raise TypeError(error_msg)

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
