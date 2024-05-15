#!/usr/bin/python3
"""np_mult"""


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.

    Returns:
        numpy.ndarray: The result of multiplying mat1 with mat2.
    """
    m = len(mat1)
    n = len(mat2[0])
    p = len(mat2)

    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for k in range(p):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
