#!/usr/bin/env python3
"""Module for derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for c in poly:
        if not isinstance(c, (int, float)) or isinstance(c, bool):
            return None
    if len(poly) == 1:
        return [0]
    deriv = [i * poly[i] for i in range(1, len(poly))]
    if all(c == 0 for c in deriv):
        return [0]
    return deriv
