#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with each element divided.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, or
                   if rows in the matrix are of different sizes, or
                   if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
