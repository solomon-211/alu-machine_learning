#!/usr/bin/env python3
"""Module that performs element-wise operations on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication,
    and division.

    Args:
        mat1: an array-like object interpretable as a numpy.ndarray.
        mat2: an array-like object interpretable as a numpy.ndarray.

    Returns:
        A tuple containing the element-wise sum, difference,
        product, and quotient of mat1 and mat2, respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
