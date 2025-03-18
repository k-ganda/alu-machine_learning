#!/usr/bin/env python3
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100,
               alpha=0.1, gamma=0.99):
    """
    Performs the TD(λ) algorithm to update the value function.

    Args:
        env: The OpenAI environment instance.
        V: A numpy.ndarray of shape (s,) containing the value estimate.
        policy: A function that takes in a state and returns the next action to take.
        lambtha: The eligibility trace factor (λ).
        episodes: The total number of episodes to train over (default: 5000).
        max_steps: The maximum number of steps per episode (default: 100).
        alpha: The learning rate (default: 0.1).
        gamma: The discount rate (default: 0.99).

    Returns:
        V: The updated value estimate.
    """
    # Initialize eligibility trace
    eligibility_trace = np.zeros_like(V)

    for _ in range(episodes):
        state = env.reset()[0]  # Assuming reset() returns (state, info)
        for _ in range(max_steps):
            action = policy(state)
            next_state, reward, done, _ = env.step(action)

            # Update eligibility trace
            eligibility_trace *= lambtha * gamma
            eligibility_trace[state] += 1

            # Compute TD error and update value estimate
            td_error = reward + gamma * V[next_state] - V[state]
            V += alpha * td_error * eligibility_trace

            state = next_state
            if done:
                break

    return V
