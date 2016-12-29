import numpy as np
import pandas as pd


def crit_func_sml(probs, obs_data, num_sim):
    """ Criterion function for simulated Maximum-Likelihood estimation.
    """

    obs_counts = np.sum(obs_data, axis=0).tolist()
    num_sides = len(obs_counts)

    sim_data = simulate_sample(num_sim, probs)
    sim_probs = (np.sum(sim_data, axis=0) / num_sim).tolist()

    rslt = 0
    for j in range(num_sides):
        rslt += obs_counts[j] * np.log(sim_probs[j])

    return -rslt


def simulate_sample(num_draws, probs):
    """ Simulate a sample of random draws.
    """

    num_sides = len(probs)

    data = np.zeros((num_draws, num_sides))

    for i in range(num_draws):
        j = np.random.choice(range(num_sides), p=probs)
        data[i, j] = 1

    df = pd.DataFrame(data)

    return df


def crit_func_ml(probs, obs_data):
    """ Criterion function for Maximum-Likelihood estimation.
    """

    counts = np.sum(obs_data, axis=0).tolist()
    num_sides = obs_data.shape[1]
    rslt = 0
    for j in range(num_sides):
        rslt += counts[j] * np.log(probs[j])

    return -rslt

def crit_func_mm(probs, obs_data):

    num_draws = obs_data.shape[0]

    obs_probs = (np.sum(obs_data, axis=0) / num_draws).tolist()
    exp_probs = probs

    print(obs_probs, exp_probs, probs)

    return np.sum((obs_probs - exp_probs) ** 2)


def crit_func_msm(probs, obs_data, num_sim):

    num_draws = obs_data.shape[0]

    obs_counts = np.sum(obs_data, axis=0) / num_draws

    sim_data = simulate_sample(num_sim, probs)
    sim_counts = np.sum(sim_data, axis=0)/num_sim

    return float(np.sum((obs_counts - sim_counts) ** 2))

def scaling(first, second):

    min_ml = np.min(np.concatenate((first, second)))
    first = first - min_ml
    second = second - min_ml
    max_ml = np.max(np.concatenate((first, second)))
    first = first / max_ml
    second = second / max_ml

    return first, second