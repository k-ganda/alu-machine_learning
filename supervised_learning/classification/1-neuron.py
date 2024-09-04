#!/usr/bin/python3
"""Importing numpy"""


import numpy as np


class Neuron:
    """Initializing the class"""
    def __init__(self, nx):
        """
        nx: number of input features
        Private instance attributes:
        __W: weights vector for neuron
        __b: bias of neuron
        __A: activated output
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    def get_W(self):
        """Getter function"""
        return self.__W

    def get_b(self):
        """Getter function b"""
        return self.__b

    def get_A(self):
        """Getter function A"""
        return self.__A
