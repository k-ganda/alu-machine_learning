#!/usr/bin/env python3

"""
A module containing a function that
calculates the marginal probability
"""

import numpy as np
likelihood = __import__('0-likelihood').likelihood


def marginal(x, n, P, Pr):
    """
    calculates the marginal probability of
    obtaining the data

    x- number of patients that develop side effects
    n- total number of patients observed
    P- 1D numpy.ndarray containing the various hypothetical
         probabilities of developing side effects
    Pr- 1D numpy.ndarray containing the prior beliefs of P

    Returns: the marginal probability of obtaining x and n
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or len(Pr.shape) != 1:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if not np.shape(P) == np.shape(Pr):
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if not np.all((P >= 0) & (P <= 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    if not np.all((Pr >= 0) & (Pr <= 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    #  formula for marginal probability:
    # # P(X/N) = P(N/X) * P(X) / P(N)
    #  P(N/X) = likelihood
    #  P(X) = Pr
    #  P(N) = marginal probability
    #  P(N) = sum(likelihood * Pr)

    return np.sum(likelihood(x, n, P) * Pr)
