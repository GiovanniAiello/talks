""" This module contains some basic functions that are useful during the
illustration.
"""

# SciPy Stack
import numpy as np


def generate_random_request():
    """ Generate a random admissible request.
    """
    # Draw random deviates that honor the constraints for the utility
    # function and distribution of returns.
    alpha, shape = np.random.uniform(low=0.0001, size=2)
    # Draw a random integration technique.
    technique = np.random.choice(['naive_mc', 'quad'])
    # Add options.
    int_options = dict()
    int_options['naive_mc'] = dict()
    int_options['naive_mc']['implementation'] = np.random.choice(['slow', 'fast'])
    int_options['naive_mc']['num_draws'] = np.random.random_integers(10, 1000)
    int_options['naive_mc']['seed'] = np.random.random_integers(10, 1000)

    # Finishing
    return alpha, shape, technique, int_options
