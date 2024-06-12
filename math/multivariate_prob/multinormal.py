#!/usr/bin/env python3
"""Module numpy being imported"""
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
        self.mean = np.mean(self.data, axis=1, keepdims=True)
        centered_data = self.data - self.mean
        self.cov = np.matmul(centered_data, centered_data.T) / (n - 1)
