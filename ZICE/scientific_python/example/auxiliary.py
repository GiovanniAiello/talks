""" This module contains some auxiliary functions.
"""

# standard library
import numpy as np


def random_sample(betas, num_agents):
    """ Draw a random sample.
    """
    # Construct auxiliary objects.
    num_covars = betas.shape[0]

    # Set a random seed to ensure recomputability in light of randomness
    np.random.seed(123)

    # Sample exogenous agent characteristics from a uniform distribution in
    # a given shape
    X = np.random.rand(num_agents, num_covars)

    # Sample random disturbances from a standard normal distribution and rescale
    eps = np.random.normal(scale=0.1, size=num_agents)

    # Construct endogenous agent characteristic
    Y = 0.1 + np.dot(X, betas) + eps

    # Finishing
    return Y, X
