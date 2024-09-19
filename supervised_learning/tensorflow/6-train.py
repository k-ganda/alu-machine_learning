#!/usr/bin/env python3
"""Importing modules"""
import tensorflow as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes,
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """
    Function that builds, trains, and saves NN classifier
    X_train: np.ndarray(training input data)
    Y_train: np.ndarray(training labels)
    X_valid: Contains validation input data
    Y_valid: Contains validation labels
    layer_sizes: list with no of nodes in each layer
    activations: list with activation functions
    alpha: the learning rate
    iterations: number of iterations to train over
    save_path designates where to save the model
    """
    # Creating placeholders for input data and labels
    nx = X_train.shape[1]
    classes = Y_train.shape[1]
    x, y = create_placeholders(nx, classes)

    # Building forward prop graph
    y_pred = forward_prop(x, layer_sizes, activations)

    # Calculate loss and accuracy
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)

    # define optimizer &train op
    train_op = create_train_op(loss, alpha)

    # Adding placeholders, tensors, operation to collection
    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('train_op', train_op)

    # Initialize the variables
    init = tf.global_variables_initializer()

    # Create a Saver object to save the model
    saver = tf.train.Saver()

    # Start the session
    with tf.Session() as sess:
        sess.run(init)

        # Training loop
        for epoch in range(iterations + 1):  # Include the 0th iteration
            # Run the optimizer and calculate the loss
            _, epoch_loss = sess.run([train_op, loss], feed_dict={x: X_train, y: Y_train})

            # Every 100 iterations (including 0th), print the training and validation stats
            if epoch % 100 == 0:
                # Calculate training accuracy
                epoch_accuracy = sess.run(accuracy, feed_dict={x: X_train, y: Y_train})
                
                # Calculate validation loss and accuracy
                valid_loss = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
                valid_accuracy = sess.run(accuracy, feed_dict={x: X_valid, y: Y_valid})

                # Print the progress
                print(f"After {epoch} iterations:")
                print(f"\tTraining Cost: {epoch_loss}")
                print(f"\tTraining Accuracy: {epoch_accuracy}")
                print(f"\tValidation Cost: {valid_loss}")
                print(f"\tValidation Accuracy: {valid_accuracy}")

        # After training, save the model
        save_path = saver.save(sess, save_path)

    # Return the path where the model was saved
    return save_path
