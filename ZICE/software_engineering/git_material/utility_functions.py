""" This module contains a variety of utility functions.
"""

# project library
from checks import basic_checks


def baseline_utility(x, alpha):
    """ This function returns the baseline utility.
    """
    # Guard interface.
    assert basic_checks('baseline_utility', 'in', x, alpha)

    # Calculate utility.
    rslt = x ** alpha

    # Check result.
    assert basic_checks('baseline_utility', 'out', rslt)

    # Finishing
    return rslt
