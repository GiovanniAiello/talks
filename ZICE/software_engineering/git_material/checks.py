""" This module contains some basic tests for the integrity of the input and
output arguments of functions.
"""

# standard library
from functools import partial

# SciPy Stack
import numpy as np


def basic_checks(name, which, *args):
    """ Some basic checks.
    """
    # Guard interface.
    assert (which in ['in', 'out'])
    # Run relevant set of checks based on function name and code section.
    if name == 'baseline_utility':
        if which == 'in':
            # Distribute arguments
            x, alpha = args
            # Perform checks.
            assert (isinstance(alpha, float))
            assert (alpha >= 0.0)
            assert (isinstance(x, float))
            assert (x >= 0.0)
        elif which == 'out':
            # Distribute arguments.
            rslt, = args
            # Perform check.
            assert (isinstance(rslt, float))
            assert (rslt > 0.0)
        else:
            raise AssertionError
    elif name == 'naive_monte_carlo':
        if which == 'in':
            # Distribute arguments.
            ((func, bounds, num_draws, implementation, seed),) = args
            # Perform checks.
            assert (implementation in ['fast', 'slow'])
            assert (isinstance(func, partial))
            assert (isinstance(num_draws, int))
            assert (num_draws > 0)
            assert (isinstance(seed, int))
            assert (seed > 0)
            assert (bounds[0] < bounds[1])
        elif which == 'out':
            # Distribute arguments.
            rslt, = args
            # Perform checks.
            assert (isinstance(rslt, float))
            assert (np.isfinite(rslt))
        else:
            raise AssertionError
    elif name == 'get_baseline_lognormal':
        if which == 'in':
            # Distribute arguments.
            ((alpha, shape, technique, int_options),) = args
            # Perform checks.
            assert (check_integration_options(technique, int_options))
            assert (technique in ['naive_mc', 'quad'])
            assert (isinstance(shape, float))
            assert (isinstance(alpha, float))
            assert (shape > 0.00)
            assert (alpha >= 0.00)
        elif which == 'out':
            # Distribute arguments.
            rslt, = args
            # Perform checks.
            assert (isinstance(rslt, float))
            assert (rslt > 0.0)
        else:
            raise AssertionError
    elif name == '_wrapper_baseline':
        if which == 'in':
            # Distribute arguments.
            alpha, shape, x = args
            # Perform checks.
            assert (isinstance(shape, float))
            assert (isinstance(alpha, float))
            assert (shape > 0.00)
            assert (alpha >= 0.00)
        elif which == 'out':
            # Distribute arguments.
            rslt, = args
            # Perform checks,
            assert (isinstance(rslt, float))
            assert (rslt >= 0.0)
        else:
            raise AssertionError
    else:
        raise AssertionError

    # Finishing
    return True


def check_integration_options(technique, int_options):
    """ This function checks the specified integration options.
    """

    if technique == 'naive_mc':
        assert  (int_options['naive_mc']['implementation'] in ['slow', 'fast'])
        assert (isinstance(int_options['naive_mc']['num_draws'], int))
        assert (int_options['naive_mc']['num_draws'] > 0)
        assert (isinstance(int_options['naive_mc']['seed'], int))
        assert (int_options['naive_mc']['seed'] > 0)

    # Finishing
    return True
