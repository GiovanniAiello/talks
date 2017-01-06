""" This module allows to illustrate alternative estimation techniques for structural estimation.
All is based on a simple binary Probit model.
"""

import numpy as np

from auxiliary import simulate_sample
from auxiliary import criterion_ml
from auxiliary import criterion_mm

from graphs import graphs_smoothing_functions
from graphs import graphs_maximum_likelihood
from graphs import graphs_method_moments

# First of all we need to simulate a sample of observed data.
data_obs, _ = simulate_sample(0.0, 100000, 465)

# This loop shows how the number of simulations smoothes out the likelihood function.
for num_sim in [100, 10000]:
    grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
    classical_values = np.apply_along_axis(criterion_ml, 0, grid, data_obs, 'classical')
    simulated_values = np.apply_along_axis(criterion_ml, 0, grid, data_obs, 'simulated', num_sim)
    graphs_maximum_likelihood(grid[0], classical_values, simulated_values, num_sim)

# The same is true for the method of moments.
grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
classical_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'classical')
simulated_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'simulated', 100, 0.00)
graphs_method_moments(grid[0], classical_values, simulated_values, 100)

# Now we also check the it for the smoothing function.
grid = np.array(np.linspace(-0.5, 0.5, 100), ndmin=2)
classical_values = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'classical')
smoothing_1 = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'simulated', 100, 0.00)
smoothing_2 = np.apply_along_axis(criterion_mm, 0, grid, data_obs, 'smoothed', 100, 0.50)
graphs_smoothing_functions(grid[0], classical_values, smoothing_1, smoothing_2)
