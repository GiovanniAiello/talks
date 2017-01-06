from scipy.stats import norm
import numpy as np


def simulate_sample(theta, num_obs, seed=123):
    """ This function simulates a sample for further analysis.
    """
    np.random.seed(seed)

    # We need to  generate containers for the latent utilities and the obseved choices.
    u = np.tile(np.nan, (num_obs, 2))
    d = np.tile(np.nan, num_obs)

    # Now we simply draw a set of random observations.
    for i in range(num_obs):
        eps = np.random.normal()
        u[i, :] = [0, theta + eps]
        d[i] = np.argmax(u[i, :])

    return d, u


def criterion_ml(theta, data_obs, type_, num_sim=None):
    """ This function allows to evaluate the criterion for maximum likelihood estimation.
    """
    if type_ == 'classical':
        probs = norm.cdf(theta)
    elif type_ == 'simulated':
        data_sim, _ = simulate_sample(theta, num_sim)
        probs = np.mean(data_sim)
    else:
        raise AssertionError('Invalid request')

    rslt = data_obs * np.log(probs) + (1.0 - data_obs) * np.log(1.0 - probs)

    return np.sum(rslt)


def get_smoothed_probabilities(u, lambda_):
    """ This function simply applys the smoothing function to the latent utilites.
    """
    num_sim = u.shape[0]

    u_smoothed = np.tile(np.nan, (num_sim, 2))

    for i in range(num_sim):
        for j in range(2):
            u_smoothed[i, j] = np.exp(u[i, j] / lambda_) / (np.exp(u[i, 0] / lambda_) + np.exp(u[i, 1] / lambda_))

    return u_smoothed


def criterion_mm(theta, data_obs, type_, num_sim=None, lambda_=1.0):
    """ This function allows to evaluate the criterion function for the method of moments.
    """
    if type_ == 'classical':
        stat = norm.cdf(theta)[0]
    elif type_ == 'simulated':
        data_sim, _ = simulate_sample(theta, num_sim)
        stat = np.mean(data_sim)
    elif type_ == 'smoothed':
        _, u = simulate_sample(theta, num_sim)
        stat = np.mean(get_smoothed_probabilities(u, lambda_), axis=0)[1]
    else:
        raise AssertionError('Invalid request')

    rslt = (np.mean(data_obs) - stat) ** 2

    return rslt
