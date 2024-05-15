#!/usr/bin/env python3
"""Concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays

    Args:
        arr1, arr2

    Returns:
        list: A new 2D list representing the concat of two arrays.

    """
    result = []
    result.append(arr1 + arr2)
    return result
