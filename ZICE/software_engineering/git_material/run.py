""" This modules allows to calculate the expected utility for a number of
utility functions, return distributions, and integration strategies.
"""

# project library
from eu_calculations import get_baseline_lognormal

""" Specify Request
"""

# Utility Function
alpha = 0.01

# Distribution of Returns
shape = 0.01

# Integration
technique = 'naive_mc'

int_options = dict()
int_options['naive_mc'] = dict()
int_options['naive_mc']['implementation'] = 'slow'
int_options['naive_mc']['num_draws'] = 1000

""" Calculate expected utility
"""

get_baseline_lognormal(alpha, shape, technique, int_options)
