#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given number.
    It returns a new matrix with the result of the division.
    It raises a TypeError exception if the matrix is not a list of lists
    of integers or floats,
    or if the rows of the matrix are not of the same size,
    or if the div is not a number.
    It raises a ZeroDivisionError exception if the div is equal to zero.
    It rounds the result of the division to 2 decimal places.
    """
    if not isinstance(
            matrix, list) or not matrix or not all(
                    isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    """
    Check if the rows of the matrix are of the same size
    """
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    """
    Check if the div is a number
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
