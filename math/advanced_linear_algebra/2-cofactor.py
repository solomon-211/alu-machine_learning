#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix."""


minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix.

    Args:
        matrix: a list of lists whose cofactor matrix should be
            calculated.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.

    Returns:
        The cofactor matrix of matrix.
    """
    minor_matrix = minor(matrix)
    return [
        [minor_matrix[i][j] * (-1) ** (i + j)
         for j in range(len(minor_matrix[i]))]
        for i in range(len(minor_matrix))
    ]
