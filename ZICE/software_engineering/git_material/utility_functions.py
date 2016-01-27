""" This module contains a variety of utility functions.
"""


def baseline_utility(x, alpha):
    """ This function returns the baseline utility.
    """
    # Guard interface.
    assert (isinstance(alpha, float))
    assert (alpha > 0.0)
    assert (isinstance(x, float))
    assert (x >= 0.0)

    # Calculate utility.
    utility = x ** alpha

    # Check result.
    assert (isinstance(utility, float))
    assert (utility > 0.0)

    # Finishing
    return utility
