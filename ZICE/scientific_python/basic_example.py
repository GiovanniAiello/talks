""" This is an implementation of the ``Basic Example'' as a Python script.
"""

# Import relevant libraries from the SciPy Stack
import matplotlib.pyplot as plt
import statsmodels.api as sm

import numpy as np

""" Setting up parametrization.
"""
# Specify parametrization
num_agents = 1000
num_covars = 3

betas_true = np.array([0.22, 0.30, -0.1]).T

""" Random Number Generation
"""
# Set a random seed to ensure recomputability in light of randomness
np.random.seed(123)

# Sample exogenous agent characteristics from a uniform distribution in
# a given shape
X = np.random.rand(num_agents, num_covars)

# Sample random disturbances from a standard normal distribution and rescale
eps = np.random.normal(scale=0.1, size=num_agents)

# Construct endogenous agent characteristic
Y = 0.1 + np.dot(X, betas_true) + eps

""" Data Visualization
"""
# Initialize canvas
ax = plt.figure(figsize=(12, 8)).add_subplot(111, axisbg='white')

# Plot synthetic sample
ax.plot(np.dot(X, betas_true), Y, 'o')

# Set axis labels and ranges
ax.set_xlabel(r'$X\beta$', fontsize=20)
ax.set_ylabel(r'$Y$', fontsize=20)

# Remove first element on y-axis
ax.yaxis.get_major_ticks()[0].set_visible(False)

# Add title
plt.suptitle('Synthetic Sample', fontsize=20)

# Save figure
plt.savefig('images/scatterplot.png', bbox_inches='tight', format='png')

""" Statistical Analysis
"""
# Add an intercept to array of exogenous variables
X = sm.add_constant(X)

# Specify and fit the model
rslt = sm.OLS(Y, X).fit()

# Provide some summary
print(rslt.summary())
