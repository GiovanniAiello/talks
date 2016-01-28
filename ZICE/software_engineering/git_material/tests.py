""" This module contains some basic tests.
"""

# SciPy Stack
from scipy.stats import lognorm

import numpy as np

# other libraries
import pytest

# project library
from eu_calculations import get_baseline_lognormal
from auxiliary import generate_random_request

# ensure recomputability
np.random.seed(123)


""" Some basic testing of our illustrative routines.
"""


def test_random_requests():
    """ Draw a whole host of random requests to ensure that the function
    works for all admissible values.
    """
    for _ in range(100):
        # Generate random request.
        alpha, shape, technique, int_options = generate_random_request()
        # Perform calculation.
        get_baseline_lognormal(alpha, shape, technique, int_options)


def test_invalid_request():
    """ Test that assertions are raised in case of a flawed request.
    """
    with pytest.raises(AssertionError):
        # Generate random request.
        alpha, shape, technique, int_options = generate_random_request()
        # Invalidate request.
        technique = 'gaussian_quadrature'
        # Parameters outside defined ranges.
        get_baseline_lognormal(alpha, shape, technique, int_options)


def test_closed_form():
    """ Test whether the results line up with a closed form solution for the
    special case, where alpha is set to zero.
    """
    # Generate a random request.
    _, shape, technique, int_options = generate_random_request()
    # Restrict to special case.
    alpha, shape = 0.0, 0.001
    # Calculate closed form solution and simulate special case.
    closed_form = lognorm.mean(shape)
    simulated = get_baseline_lognormal(alpha, shape, technique, int_options)
    # Test equality.
    np.testing.assert_almost_equal(closed_form, simulated, decimal=3)


def test_regression():
    """ This regression test ensures that the code does not change during
    refactoring without noticing.
    """
    # Set seed to avoid dependence of seed.
    np.random.seed(123)
    # Generate random request.
    alpha, shape, technique, int_options = generate_random_request()
    # Perform calculation.
    rslt = get_baseline_lognormal(alpha, shape, technique, int_options)
    # Ensure equivalence with expected results up to numerical precision.
    np.testing.assert_almost_equal(rslt, 0.65222028429023948)