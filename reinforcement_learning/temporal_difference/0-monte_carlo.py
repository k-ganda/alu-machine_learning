#!/usr/bin/env python3
"""Importing libraries"""
import numpy as np
import gym


def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """
    Performs monte carlo algorithm
    env: environment instance
    V: (s,) value estimate
    policy: takes state return action
    """
    for episode in range(episodes):
        state = env.reset()
        episode_history = []
        for step in range(max_steps):
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            episode_history.append((state, reward))
            state = next_state
            
            if done:
                break

        G = 0
        for state, reward in reversed(episode_history):
            G = gamma * G + reward
            V[state] += alpha * (G - V[state])
    return V
