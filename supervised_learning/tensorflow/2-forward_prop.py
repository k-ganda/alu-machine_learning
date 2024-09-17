#!/usr/bin/env python3
"""Importing tensorflow"""
import tensorflow as tf
# Import the create_layer function
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Create the forward propagation graph for the neural network.
    x: placeholder for the input data
    layer_sizes: number of nodes in that layer
    activations: activation function for that layer
    Returns: tensor of the final layer's output
    """
    # Initialize the input tensor
    prev = x

    # Ensure that layer_sizes and activations are of the same length
    if len(layer_sizes) != len(activations):
        raise ValueError("The length of layer_sizes must
                         match the length of activations")

    # Create each layer using create_layer function
    for i in range(len(layer_sizes)):
        prev = create_layer(prev, layer_sizes[i], activations[i])

    # The final tensor is the prediction of the network
    return prev
