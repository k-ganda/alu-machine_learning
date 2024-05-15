import numpy as np

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.

    Returns:
        tuple: The element-wise sum, difference, product, and quotient of mat1 and mat2.
    """
    elementwise_sum = mat1 + mat2
    elementwise_diff = mat1 - mat2
    elementwise_product = mat1 * mat2
    elementwise_quotient = mat1 / mat2
    
    return elementwise_sum, elementwise_diff, elementwise_product, elementwise_quotient
