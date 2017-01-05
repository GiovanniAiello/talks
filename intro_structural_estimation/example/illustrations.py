#!/usr/bin/env python

from criterion_functions import *


from graphs import graphs_smoothing_functions
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


# # First I create a set of graphs with only 100 simulated draws for the
# # simulation counterpart.
# ml_values = np.apply_along_axis(crit_func_ml, 1, prob, obs_data)
# sml_values = np.apply_along_axis(crit_func_sml, 1, prob, obs_data, 100)
# ml_values, sml_values = scaling(ml_values, sml_values)
# graphs_maximum_likelihood(prob_1, ml_values, sml_values, 100)
#
# mm_values = np.apply_along_axis(crit_func_mm, 1, prob, obs_data)
# msm_values = np.apply_along_axis(crit_func_msm, 1, prob, obs_data, 100)
# mm_values, msm_values = scaling(mm_values, msm_values)
# graphs_method_moments(prob_1, mm_values, msm_values, 100)
#
# # I now create a new graphs of maximum likelihood estimation with 1,000
# # simulated draws.
# ml_values = np.apply_along_axis(crit_func_ml, 1, prob, obs_data)
# sml_values = np.apply_along_axis(crit_func_sml, 1, prob, obs_data, 1000)
# ml_values, sml_values = scaling(ml_values, sml_values)
# graphs_maximum_likelihood(prob_1, ml_values, sml_values, 1000)

# Now I also want to illustrate the workings of a smoothing function.
def smoothing(x, lambda_):

    return np.exp(x / lambda_) / (1 + np.exp(x / lambda_))

df = simulate_sample(1, [0.8, 0.2],seed=14536)

#
# grid = np.linspace(-3, 3, 250, True)
#
# values_0_10 = np.apply_along_axis(smoothing, 0, grid, 0.10)
# values_0_25 = np.apply_along_axis(smoothing, 0, grid, 0.25)
# values_0_75 = np.apply_along_axis(smoothing, 0, grid, 0.75)
#
# graphs_smoothing_functions(grid, values_0_10, values_0_25, values_0_75)


def smoothed_probabilities(probs):

    num_sim = 100
    num_sides = len(probs)

    draws = np.random.logistic(size=(num_sim, num_sides))

    print(draws.shape)
    grid = np.tile(np.nan, (num_sim, num_sides))


    for i in range(num_sim):

        grid[i, :] = probs + draws[i, :]





smoothed_probabilities([0.5, 0.5])