#!/usr/bin/env python3
"""Module that calculates the adjugate matrix of a matrix."""


cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix.

    Args:
        matrix: a list of lists whose adjugate matrix should be
            calculated.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.

    Returns:
        The adjugate matrix of matrix.
    """
    cofactor_matrix = cofactor(matrix)
    size = len(cofactor_matrix)
    return [
        [cofactor_matrix[j][i] for j in range(size)]
        for i in range(size)
    ]
