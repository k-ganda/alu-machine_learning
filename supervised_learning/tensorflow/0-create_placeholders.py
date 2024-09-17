#!/usr/bin/env python3
"""Importing tensorflow"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Function that returns two placeholders
    nx: No of feature columns
    classes: no of classes in classifier
    Returns:
    x: Placeholder for input
    y: placeholder for one-hot labels(input)
    """
    x = tf.placeholder(tf.float32, shape=(None, nx),
                       name="x")
    y = tf.placeholder(tf.float32, shape=(None, classes),
                       name="y")
    return x, y
