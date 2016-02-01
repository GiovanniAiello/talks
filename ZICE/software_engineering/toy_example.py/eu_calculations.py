""" This module computes the expected utility.
"""

# standard library
from functools import partial

# SciPy Stack
from scipy.stats import lognorm

import scipy.integrate as integrate

# project library
from integration_rules import naive_monte_carlo
from utility_functions import baseline_utility

# testing library
from testing.checks import basic_checks


""" Baseline Utility, Lognormal Returns, Naive Monte Carlo
"""


def get_baseline_lognormal(alpha, shape, technique, int_options):
    """ Get the expected returns by drawing numerous random deviates from a
    lognormal distribution.
    """
    # Guard interface.
    args = (alpha, shape, technique, int_options)
    assert basic_checks('get_baseline_lognormal', 'in', args)

    # Construct bounds based on quantiles of lognormal distribution.
    lower, upper = 0, lognorm.ppf(0.9999999, shape)

    # Prepare wrapper for alternative integration strategies.
    func = partial(_wrapper_baseline, alpha, shape)
    # Perform native monte carlo integration.
    if technique == 'naive_mc':
        # Distribute relevant integration options.
        implementation = int_options['naive_mc']['implementation']
        num_draws = int_options['naive_mc']['num_draws']
        seed = int_options['naive_mc']['seed']
        # Perform naive Monte Carlo integration.
        rslt = naive_monte_carlo(func, (lower, upper), num_draws,
                                 implementation, seed)
    elif technique == 'quad':
        # Perform integration based on quadrature.
        rslt = integrate.quad(func, lower, upper)[0]
    else:
        pass

    # Check result.
    assert basic_checks('get_baseline_lognormal', 'out', rslt)

    # Finishing
    return rslt


def _wrapper_baseline(alpha, shape, x):
    """ This private function constructs the integrand for the application of
    numerical integration strategies.
    """
    # Guard interface.
    assert basic_checks('_wrapper_baseline', 'in', alpha, shape, x)

    # Evaluate utility and weigh by probability.
    rslt = baseline_utility(x, alpha) * lognorm.pdf(x, shape)

    # Check result.
    assert basic_checks('_wrapper_baseline', 'out', rslt)

    # Finishing
    return rslt

