#!/usr/bin/env python3
"""Determinant of a matrix"""
import numpy as np


def determinant(matrix):
    """
    Find the detrminant of a (0,0) matrix
    Arg:
    matrix
    Returns:
        Determinant of the matrix
    """
    # Base cases for determinants of 0x0, 1x1, and 2x2 matrice
    if matrix != [[]]:
        raise TypeError("matrix must be a list of lists")

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if matrix == [[]]:
        return 1

    np_matrix = np.array(matrix)
    det = np.linalg.det(np_matrix)

    return round(det)
