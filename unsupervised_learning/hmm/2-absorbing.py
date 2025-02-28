#!/usr/bin/env python3

"""
This module determines if markov chain
is absorbing"""

import numpy as np


def absorbing(P):
    """
    Determines whether a Markov chain is absorbing.

    P - square 2D numpy.ndarray: (n, n) transition matrix
        - P[i, j] is the probability of transitioning from
        state i to state j
        - n is the number of states in the Markov chain

    Returns: True if it is absorbing, False otherwise
    """
    if len(P.shape) != 2:
        return False
    n1, n2 = P.shape
    if n1 != n2 or type(P) is not np.ndarray:
        return False

    # Check if there is at least one absorbing state
    absorbing_states = [
        i for i in range(n1) if P[i, i] == 1 and np.all(P[i, :] == 0)
    ]

    # If no absorbing states are found, return False
    if len(absorbing_states) == 0:
        return False

    # Markov chain is absorbing if at least one absorbing state exists
    return True
