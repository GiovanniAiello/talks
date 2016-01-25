""" This module contains a variety of integration rules.
"""

# standard library
from types import FunctionType


def monte_carlo_integration(func, num_draws=10000):
    """ This function performs a Monte Carlo integration.
    """
    # Guard interface
    assert (isinstance(func, FunctionType))
    assert (isinstance(num_draws, int))
    assert (num_draws > 0)

    #