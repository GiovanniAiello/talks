""" This modules allows to calculate the expected utility for a number of
utility functions, return distributions, and integration strategies.
"""

# project library
from eupy import get_baseline_lognormal

""" Specify Request
"""

# Utility Function
alpha = 0.01

# Distribution of Returns
shape = 0.01

# Integration techniques
technique = 'quad'

int_options = dict()
if technique == 'naive_mc':
    int_options['naive_mc'] = dict()
    int_options['naive_mc']['implementation'] = 'slow'
    int_options['naive_mc']['num_draws'] = 1000
    int_options['naive_mc']['seed'] = 123

""" Calculate expected utility
"""
rslt = get_baseline_lognormal(alpha, shape, technique, int_options)

print(' Expected Utility {}'.format(rslt))