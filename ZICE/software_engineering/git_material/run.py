""" This modules allows to calculate the expected utility for a number of
utility functions, return distributions, and integration strategies.
"""

# TODO: This is wrong, refers to determination of upper bound for MC.
# TODO: unit test battery ... take and align with notebook.

# project library
from eu_calculations import get_baseline_lognormal_naive

""" Specify Request
"""

# Utility Function
alpha = 0.01

# Distribution of Returns
mean, sd = 0.01, 1.0

# Integration
num_draws = 1000

""" Calculate expected utility
"""

get_baseline_lognormal_naive(alpha, mean, sd, num_draws)
