""" This module contains some auxiliary functions.
"""

# SciPy Stack
import numpy as np

def get_random_deviates(mean, sd, num_draws):
    """ Get random deviates from a lognormal
    distribution.
    """
    # Draw deviates from lognormal distribution.
    deviates = []
    for _ in range(num_draws):
        deviate = np.random.lognormal(mean, sd)
        deviates += [deviate]

    # Type Conversion
    deviates = np.array(deviates)

    # Finishing
    return deviates