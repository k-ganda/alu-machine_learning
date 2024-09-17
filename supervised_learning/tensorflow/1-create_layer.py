#!/usr/bin/env python3
"""Importing tensorflow"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """
    prev: tensor output of previous
    n: no of nodes in layer
    activation: activation function
    Returns: tensor output
    """
    # He et al initializer for weights
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")

    #Creating the layer
    layer = tf.layers.dense(inputs=prev,
                            units=n,
                            activation=activation,
                            kernel_initializer=initializer,
                            name="layer")
    return layer
