""" This module computes the expected utility.
"""

# standard library
from functools import partial

# SciPy Stack
from scipy.stats import lognorm

# project library
from integration_rules import naive_monte_carlo
from utility_functions import baseline_utility
from checks import basic_checks


""" Baseline Utility,Lognormal Returns, Naive Monte Carlo
"""


def get_baseline_lognormal_naive(alpha, mean, sd, num_draws):
    """ Get the expected returns by drawing numerous random deviates from a
    lognormal distribution.
    """
    # Guard interface.
    args = (alpha, mean, sd, num_draws)
    assert basic_checks('get_baseline_lognormal_naive', 'in', args)

    # Construct bounds based on quantiles of lognormal distribution.
    lower, upper = 0, lognorm.ppf(0.975, 1.0)

    # Prepare wrapper for integration strategy.
    func = partial(_wrapper_baseline, alpha, mean, sd)

    # Perform native monte carlo integration.
    rslt = naive_monte_carlo(func, (lower, upper), num_draws)

    # Check result.
    assert basic_checks('get_baseline_lognormal_naive', 'out', rslt)

    # Finishing
    return rslt


def _wrapper_baseline(alpha, mean, sd, x):
    """ This private function constructs the integrand for the application of
    numerical integration strategies.
    """
    # Guard interface.
    assert basic_checks('_wrapper_baseline', 'in', alpha, mean, sd, x)

    # Evaluate utility and weigh by probability.
    rslt = baseline_utility(x, alpha) * lognorm.pdf(mean, sd)

    # Check result.
    assert basic_checks('_wrapper_baseline', 'out', rslt)

    # Finishing
    return rslt

