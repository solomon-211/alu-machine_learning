#!/usr/bin/env python3
"""Module that calculates the shape of a matrix."""


def matrix_shape(matrix):
    """Calculate the shape of a matrix.

    Args:
        matrix: a nested list representing a matrix of any dimension.

    Returns:
        A list of integers representing the shape of the matrix.
    """
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        current = current[0] if len(current) > 0 else None
    return shape
