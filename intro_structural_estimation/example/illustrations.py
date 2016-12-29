#!/usr/bin/env python

from criterion_functions import *


from graphs import graphs_maximum_likelihood
from graphs import graphs_method_moments


np.random.seed(123)


num_draws, obs_probs = 10000, [0.50, 0.50]
obs_data = simulate_sample(num_draws, obs_probs)

num_sides = obs_data.shape[1]
start_probs = np.ones(num_sides) / num_sides


# I now create a grid with evaluation points for the two-dimensional case.
prob_1 = np.linspace(0.05, 0.95, 250, True)
prob_2 = 1 - prob_1
prob = np.array([prob_1, prob_2]).T


# First I create a set of graphs with only 100 simulated draws for the
# simulation counterpart.
ml_values = np.apply_along_axis(crit_func_ml, 1, prob, obs_data)
sml_values = np.apply_along_axis(crit_func_sml, 1, prob, obs_data, 100)
ml_values, sml_values = scaling(ml_values, sml_values)
graphs_maximum_likelihood(prob_1, ml_values, sml_values, 100)

mm_values = np.apply_along_axis(crit_func_mm, 1, prob, obs_data)
msm_values = np.apply_along_axis(crit_func_msm, 1, prob, obs_data, 100)
mm_values, msm_values = scaling(mm_values, msm_values)
graphs_method_moments(prob_1, mm_values, msm_values)

# I now create a new graphs of maximum likelihood estimation with 1,000
# simulated draws.
ml_values = np.apply_along_axis(crit_func_ml, 1, prob, obs_data)
sml_values = np.apply_along_axis(crit_func_sml, 1, prob, obs_data, 1000)
ml_values, sml_values = scaling(ml_values, sml_values)
graphs_maximum_likelihood(prob_1, ml_values, sml_values, 1000)

# Now look at