#!/usr/bin/env python3
"""Sigma summation"""


def summation_i_squared(n):
    """
    Calculates the sigma(sum)
    Arg: n(integer)
    Returns:
    integer value of sum
    """
    ssum = 0
    if type(n) != int and type(n) != float:
        return None
    else:
        for i in range(n + 1):
            ssum = ssum + i**2
        return ssum
