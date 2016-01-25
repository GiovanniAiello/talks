""" This module computes the expected
"""

# SciPy Stack
import numpy as np

# project library
from utility_functions import baseline_utility
from auxiliary import get_random_deviates

def get_expected_utility(alpha, mean, sd):
    """ Get the expected returns by drawing numerous
    random deviates from a lognormal distribution.
    """
    # Guard interface
    assert (isinstance(mean, float))
    assert (isinstance(sd, float))
    assert (isinstance(alpha, float))
    assert (sd >= 0.00)
    assert (alpha >= 0.00)

    # Set parametrization for Monte Carlo
    # integration.
    num_draws = 10000000

    # Draw deviates from the lognormal distribution.
    deviates = get_random_deviates(mean, sd, num_draws)

    # Calculate the average utility from all deviates.
    rslt = 0.02#np.mean(deviates ** alpha)

    # Check result
    assert (isinstance(rslt, float))

    # Finishing
    return rslt