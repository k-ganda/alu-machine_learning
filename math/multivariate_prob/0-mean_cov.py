#!/usr/bin/env python3
"""Importing module numpy"""


import numpy as np


def mean_cov(X):
    """
    Calulating the mean of a covariance matrix
    X is a numpy.ndarray of shape (n, d) containing the data set
    n is the number of data points
    d is the number of dimensions in each data point
    If X is not a 2D numpy.ndarray, raise a TypeError
    with the message X must be a 2D numpy.ndarray
    If n is less than 2, raise a ValueError with the
    message X must contain multiple data points
    Returns: mean, cov:
    mean is a numpy.ndarray of shape (1, d) containing the mean of the data set
    cov is a numpy.ndarray of shape (d, d)
    containing the covariance matrix of the data set
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    mean = np.mean(X, axis=0, keepdims=True)
    cov = np.matmul((X - mean).T, X - mean) / (n - 1)
    return mean, cov
