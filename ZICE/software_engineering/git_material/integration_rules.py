""" This module contains a variety of integration rules.
"""

# SciPy Stack
import numpy as np

# project library
from checks import basic_checks


def naive_monte_carlo(func, bounds, num_draws):
    """ This function performs a Monte Carlo integration.
    """
    # Guard interface.
    assert basic_checks('naive_monte_carlo', 'in', func, bounds, num_draws)

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
    assert basic_checks('naive_monte_carlo', 'out', rslt)

    # Finishing
    return rslt

