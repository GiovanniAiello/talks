""" This module allows to illustrate alternative estimation techniques for structural estimation.
All is based on a simple binary Probit model.
"""
import statsmodels.api as sm
import numpy as np

from auxiliary import logistic_function
from auxiliary import simulate_sample
from auxiliary import illustration_ii
from auxiliary import criterion_mm
from auxiliary import criterion_ml

from graphs import graphs_smoothing_functions
from graphs import graphs_distribution_shifts
from graphs import graphs_indirect_inference
from graphs import graphs_maximum_likelihood
from graphs import graphs_logistic_function
from graphs import graphs_method_moments

# First of all we need to simulate a sample of observed data and also create a grid along which
# we will evaluate the alternative criterion functions.
grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
data_obs, _ = simulate_sample(0.0, 100000, 465)

# This loop shows how the number of simulations smoothes out the likelihood function.
for num_sim in [100, 10000]:
    grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
    classical_values = np.apply_along_axis(criterion_ml, 0, grid, data_obs, 'traditional')
    simulated_values = np.apply_along_axis(criterion_ml, 0, grid, data_obs, 'AR-simulator', num_sim)
    graphs_maximum_likelihood(grid[0], classical_values, simulated_values, num_sim)

# Now let me also create a graph for the simulated method of moments.
classical_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'traditional')
simulated_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'AR-simulator', 100, 0.00)
graphs_method_moments(grid[0], classical_values, simulated_values, 100)

# Now we also check the it for the smoothing function.
classical_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'traditional')
smoothing_1 = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'AR-simulator', 100, 0.00)
smoothing_2 = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'smoothed-AR-simulator', 100, 0.50)
graphs_smoothing_functions(grid[0], classical_values, smoothing_1, smoothing_2)

# I want to fit a linear probability model to illustrate the workings of indirect inference.
grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
observed_values = np.tile(sm.OLS(data_obs, np.tile(1, len(data_obs))).fit().params[0], 100)
simulated_values = np.apply_along_axis(illustration_ii, 0, grid, 1000)
graphs_indirect_inference(grid[0], observed_values, simulated_values)

# For illustrative purposes, I also plot the logistic function. Note, that the grid needs to be
# redefined here.
grid = np.array(np.linspace(-3, 3, 100), ndmin=2)
values_0_10 = np.apply_along_axis(logistic_function, 0, grid, 0.10)
values_0_25 = np.apply_along_axis(logistic_function, 0, grid, 0.25)
values_0_75 = np.apply_along_axis(logistic_function, 0, grid, 0.75)
graphs_logistic_function(grid[0], values_0_10[0], values_0_25[0], values_0_75[0])

# I also want a graph tha that shows how the distribution of latent utilities is affect by shifts
# in the location parameter.
graphs_distribution_shifts()