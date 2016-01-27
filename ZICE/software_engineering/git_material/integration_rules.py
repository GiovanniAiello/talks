""" This module contains a variety of integration rules.
"""

# standard library
from functools import partial

# SciPy Stack
import numpy as np


def naive_monte_carlo(func, bounds, num_draws):
    """ This function performs a Monte Carlo integration.
    """
    # Guard interface.
    assert (isinstance(func, partial))
    assert (isinstance(num_draws, int))
    assert (num_draws > 0)
    assert (bounds[0] < bounds[1])

    # Distribute bounds.
    lower, upper = bounds

    # Draw requested number of deviates.
    deviates = np.random.uniform(lower, upper, size=num_draws)

    # Implement native Monte Carlo approach.
    rslt = 0.0
    for deviate in deviates:
        rslt += func(deviate)
    rslt = np.mean(rslt)

    # Check result.
    assert (isinstance(rslt, float))
    assert (np.isfinite(rslt))

    # Finishing
    return rslt

