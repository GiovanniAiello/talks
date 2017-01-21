import statsmodels.api as sm
from scipy.stats import norm
import numpy as np


def simulate_sample(theta, num_obs, seed=123):
    """ This function simulates a sample for further analysis.
    """
    np.random.seed(seed)

    # We need to  generate containers for the latent utilities and the observed choices.
    u = np.tile(np.nan, (num_obs, 2))
    d = np.tile(np.nan, num_obs)

    # Now we simply draw a set of random observations.
    for i in range(num_obs):
        eps = np.random.normal()
        u[i, :] = [0, theta + eps]
        d[i] = np.argmax(u[i, :])

    return d, u


def criterion_ml(theta, data_obs, type_, num_sim=None, seed=123):
    """ This function evaluates the criterion for traditional and simulation-based maximum
    likelihood estimation.
    """
    if type_ == 'traditional':
        probs = norm.cdf(theta)
    elif type_ == 'AR-simulator':
        data_sim, _ = simulate_sample(theta, num_sim, seed)
        probs = np.mean(data_sim)
    else:
        raise AssertionError('Invalid request')

    rslt = data_obs * np.log(probs) + (1.0 - data_obs) * np.log(1.0 - probs)

    return np.sum(rslt)


def get_smoothed_probabilities(u, lambda_):
    """ This function simply applies the Logit smoothing function to the latent utilities.
    """
    num_sim = u.shape[0]

    u_smoothed = np.tile(np.nan, (num_sim, 2))

    for i in range(num_sim):
        for j in range(2):
            u_smoothed[i, j] = np.exp(u[i, j] / lambda_) / (np.exp(u[i, 0] / lambda_) + np.exp(u[i, 1] / lambda_))

    return u_smoothed


def criterion_mm(theta, data_obs, type_, num_sim=None, lambda_=1.0):
    """ This function evaluates the criterion for traditional and simulation-based method of
    moments estimation.
    """
    if type_ == 'traditional':
        stat = norm.cdf(theta)[0]
    elif type_ == 'AR-simulator':
        data_sim, _ = simulate_sample(theta, num_sim)
        stat = np.mean(data_sim)
    elif type_ == 'smoothed-AR-simulator':
        _, u = simulate_sample(theta, num_sim)
        stat = np.mean(get_smoothed_probabilities(u, lambda_), axis=0)[1]
    else:
        raise AssertionError('Invalid request')

    rslt = (np.mean(data_obs) - stat) ** 2

    return rslt


def criterion_ii(theta, data_obs, num_sim):
    """ This function evaluates the criterion for indirect inference estimation.
    """
    # Run auxiliary model on observed data.
    beta_obs = sm.OLS(data_obs, np.tile(1, len(data_ob))).fit().params[0]

    # Simulate a dataset with candidate parametrization and run auxiliary model.
    data_sim, _ = simulate_sample(theta, num_sim)
    beta_ii = sm.OLS(data_sim, np.tile(1, len(data_sim))).fit().params[0]

    return (beta_obs - beta_ii) ** 2


def illustration_ii(theta, num_sim):
    """ This function serves to illustrate the reasoning behind indirect inference estimation.
    """
    data_sim, _ = simulate_sample(theta, num_sim)
    rslt = sm.OLS(data_sim, np.tile(1, len(data_sim))).fit().params[0]

    return rslt


def logistic_function(x, lambda_):
    """ Logistic function that allows to smooth the simulated probabilities.
    """
    return np.exp(x / lambda_) / (1 + np.exp(x / lambda_))
