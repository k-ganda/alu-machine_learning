#!/usr/bin/env python3
"""Determinant of a matrix"""


def determinant(matrix):
    """
    Find the detrminant of a (0,0) matrix
    Arg:
    matrix
    Returns:
        Determinant of the matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if rows != cols:
        raise ValueError("matrix must be a square matrix")
    if rows == 0:
        return 1
    if rows == 1:
        return matrix[0][0]
    det = 0
    for c in range(cols):
        det += ((-1) ** c) * matrix[0][c] * determinant([[matrix[r][c] for c in range(cols) if c != i] for i, r in enumerate(range(1, rows))])
    return det
