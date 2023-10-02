#!/usr/bin/python3
"""Defines matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """Returns a new matrix of matrix elements divided by div

    Args:
        matrix (list): A list of lists of int and floats
        div (int/float): Not equal to zero

    Raises:
        TypeError: If the matrix contains Non-numbers or not a list of lists
        TypeError: If the div is not an int or float
        TypeError: Each row of the matrix is not the same in size
        ZeroDivisionError: The div equals to zero

    Return:
        A new matrix of elements divided by the div
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float))
                for el in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(el/div, 2) for el in row] for row in matrix]
    return new_matrix
