#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix."""


determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Calculate the inverse of a matrix.

    Args:
        matrix: a list of lists whose inverse should be calculated.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.

    Returns:
        The inverse of matrix, or None if matrix is singular.
    """
    adjugate_matrix = adjugate(matrix)
    det = determinant(matrix)
    if det == 0:
        return None

    return [[value / det for value in row] for row in adjugate_matrix]
