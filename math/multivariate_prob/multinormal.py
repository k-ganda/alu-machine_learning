#!/usr/bin/env python3
import numpy as np
"""Class multinormal"""


class MultiNormal:
    """
    class multinormal
    """
    def __init__(self, data):
        """
        class constructor
        data is a numpy.ndarray of shape (d, n) containing the data set:
        n is the number of data points
        d is the number of dimensions in each data point
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.data = data
        self.mean = np.mean(self.data, axis=0, keepdims=True)
        self.cov = np.matmul((self.data - self.mean).T, self.data - self.mean) / (n - 1)
