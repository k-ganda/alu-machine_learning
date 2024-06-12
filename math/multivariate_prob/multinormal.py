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

    def pdf(self, x):
        """
        calculates the PDF at a data point
        d - dimensions of multinomial instance
        returns value of PDF
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy array")
        if x.shape != (self.mean.shape[0], 1):
            raise ValueError(
                'x must have the shape ({:d}, 1)'.
                format(self.mean.shape[0])
            )
        d = self.cov.shape[0]
        x_m = x - self.mean
        cov_inv = np.linalg.inv(self.cov)
        det = np.linalg.det(self.cov)
        pi = 3.1415926536
        prefactor = 1.0 / (np.sqrt((2 * pi) ** d * det))
        exponent = -0.5 * np.matmul(np.matmul(x_m.T, cov_inv), x_m)
        pdf = prefactor * np.exp(exponent)
        return pdf[0][0]
