#!/usr/bin/env python3
"""Creating a class Poisson"""


class Poisson:
    """
    represents a poisson distribution
    data is a list of the data to be used to estimate the distribution
    lambtha is the expected number of occurences in a given time frame
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Sets the instance attribute lambtha
        Saves lambtha as a float
        If data is not given, (i.e. None
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
