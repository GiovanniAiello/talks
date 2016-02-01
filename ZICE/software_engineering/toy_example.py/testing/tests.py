""" This module contains some basic tests.
"""

# SciPy Stack
from scipy.stats import lognorm

import numpy as np

import sys

# other libraries
import pytest

# project library
sys.path.append('../')
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


def test_closed_form_quad():
    """ Test whether the results line up with a closed form solution for the
    special case, where alpha is set to zero. This function test the
    quadrature implementation.
    """
    for _ in range(10):
        # Generate random request.
        alpha, shape, _, int_options = generate_random_request()
        # Restrict to special case.
        alpha, shape = 0.0, 0.001
        # Calculate closed form solution and simulate special case.
        closed_form = lognorm.mean(shape)
        simulated = get_baseline_lognormal(alpha, shape, 'quad', int_options)
        # Test equality.
        np.testing.assert_almost_equal(closed_form, simulated, decimal=3)


def test_naive_implementations():
    """ Test whether the results from the fast and slow implementation of the
    naive monte carlo integration are identical.
    """
    technique = 'naive_mc'
    for _ in range(10):
        # Generate random request.
        alpha, shape, _, int_options = generate_random_request()
        # Loop over alternative implementations.
        baseline = None
        for implementation in ['fast', 'slow']:
            int_options['naive_mc']['implementation'] = implementation
            rslt = get_baseline_lognormal(alpha, shape, technique, int_options)
            if baseline is None:
                baseline = rslt
        # Test equality.
        np.testing.assert_almost_equal(baseline, rslt)


def test_closed_form_naive():
    """ Test whether the results line up with a closed form solution for the
    special case, where alpha is set to zero. This function test the naive
    monte carlo implementation.
    """
    for _ in range(10):
        # Generate random request.
        alpha, shape, _, int_options = generate_random_request()
        # Set options favourable.
        int_options['naive_mc']['num_draws'] = 1000
        int_options['naive_mc']['implementation'] = 'fast'
        # Restrict to special case.
        alpha, shape = 0.0, 0.001
        # Calculate closed form solution and simulate special case.
        closed_form = lognorm.mean(shape)
        simulated = get_baseline_lognormal(alpha, shape, 'naive_mc', int_options)
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
    np.testing.assert_almost_equal(rslt, 0.21990743996551923)