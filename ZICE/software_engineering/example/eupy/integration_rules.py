""" This module contains a variety of integration rules.
"""

# SciPy Stack
import numpy as np

# project library
from testing.checks import basic_checks


def naive_monte_carlo(func, bounds, num_draws, implementation, seed):
    """ This function performs a Monte Carlo integration.
    """
    # Guard interface.
    args = (func, bounds, num_draws, implementation, seed)
    assert basic_checks('naive_monte_carlo', 'in', args)

    # Distribute bounds.
    lower, upper = bounds

    # Draw requested number of deviates.
    np.random.seed(seed)
    deviates = np.random.uniform(lower, upper, size=num_draws)

    # Implement native Monte Carlo approach.
    if implementation == 'slow':
        rslt = 0.0
        for deviate in deviates:
            rslt += func(deviate)
    elif implementation == 'fast':
        rslt = np.sum(np.vectorize(func)(deviates))
    else:
        raise AssertionError

    # Scaling by augmented assignment.
    rslt /= num_draws

    # Check result.
    assert basic_checks('naive_monte_carlo', 'out', rslt)

    # Finishing
    return rslt

