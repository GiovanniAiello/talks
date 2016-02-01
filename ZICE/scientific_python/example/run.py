""" This module generates a random samples, runs an OLS regression and
visualizes the results.
"""

# Import relevant libraries from the SciPy Stack
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# project library
from auxiliary import random_sample

# Specify parametrization
num_agents, num_covars = 1000, 3

betas = np.array([0.22, 0.30, -0.1]).T

# Generate random sample.
Y, X = random_sample(betas, num_agents)

# Perform a basic OLS regression and print out summary information.
rslt = sm.OLS(Y, sm.add_constant(X)).fit()
print(rslt.summary())

# Show interactive plot.
ax = plt.figure(figsize=(12, 8)).add_subplot(111, axisbg='white')

# Plot synthetic sample
ax.plot(np.dot(X, betas), Y, 'o')

# Set axis labels and ranges
ax.set_xlabel(r'$X\beta$', fontsize=20)
ax.set_ylabel(r'$Y$', fontsize=20)

# Remove first element on y-axis
ax.yaxis.get_major_ticks()[0].set_visible(False)

# Add title
plt.suptitle('Synthetic Sample', fontsize=20)

# Show figure
plt.show()
