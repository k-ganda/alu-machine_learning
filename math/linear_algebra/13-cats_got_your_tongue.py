#!/usr/bin/env python3
"""Concate"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.
        axis (int): Axis along which to concatenate.
    Returns:
        numpy.ndarray: A new matrix containing the concatenated matrices.
    """
    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        return [list(row1 + row2) for row1, row2 in zip(mat1, mat2)]
    else:
        return None
