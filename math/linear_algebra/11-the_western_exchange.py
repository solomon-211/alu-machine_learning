#!/usr/bin/env python3
"""Module that transposes a numpy.ndarray."""


def np_transpose(matrix):
    """Transpose a numpy.ndarray.

    Args:
        matrix: an array-like object interpretable as a numpy.ndarray.

    Returns:
        A new numpy.ndarray that is the transpose of matrix.
    """
    return matrix.transpose()
