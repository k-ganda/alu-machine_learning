#!/usr/bin/env python3
"""calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
    Returns integral of polynomial
    """
    if not isinstance(poly, list)
    or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    if not isinstance(C, (int, float)):
        return None

    integral = [C]

    for i in range(len(poly)):
        integral_coef = poly[i] / (i + 1)
        if integral_coef.is_integer():
            integral_coef = int(integral_coef)
        integral.append(integral_coef)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
