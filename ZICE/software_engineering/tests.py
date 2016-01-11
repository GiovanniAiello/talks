# SciPy Stack
import numpy as np


def get_expected_utility(alpha, mean, sd):
    """ Get the expected returns by drawing numerous
    random deviates from a lognormal distribution.
    """
    # Guard interface
    assert (isinstance(mean, float))
    assert (isinstance(sd, float))
    assert (isinstance(alpha, float))
    assert (sd >= 0.00)
    assert (alpha >= 0.00)
    
    # Set parametrization for Monte Carlo 
    # integration.
    num_draws = 10000000
    
    # Draw ten-thousand deviates from the 
    deviates = get_random_deviates(mean, sd, num_draws)
    
    # Calculate the average utility from all deviates.
    rslt = np.mean(np.array(deviates) ** alpha)
    
    # Check result
    assert (isinstance(rslt, float))
        
    # Finishing
    return rslt


def get_random_deviates(mean, sd, num_draws):
    """ Get random deviates from a lognormal 
    distribution.
    """
    # Draw deviates from lognormal distribution.
    deviates = []
    for _ in range(num_draws):
        deviate = np.random.lognormal(mean, sd)
        deviates += [deviate]
    
    # Finishing
    return deviates


def generate_random_request():
    """ Generate a random admissible request.
    """
    # Draw random deviates that honor the suppert
    # constraints.
    mean = np.random.normal()
    alpha, sd = np.random.uniform(size=2)

    # Finishing
    return alpha, mean, sd


def test_random_requests():
    """ Draw a whole host of random requests to
    ensure that the function works for all admissible
    values.
    """
    for _ in range(5):
        # Get expected returns.
        alpha, mean, sd = generate_random_request()
        get_expected_utility(alpha, mean, sd)


def test_results():
    """ Test some previous knowledge about the results.
    """
    for _ in range(5):
        # Get expected returns.
        alpha, mean, sd = generate_random_request()
        rslt = get_expected_utility(alpha, mean, sd)
        # Assertions
        assert rslt > 0


def test_closed_form():
    """ Test the simulated result against the closed
    form solution in the special case of linear utility.
    """
    for _ in range(1):
        _, mean, sd = generate_random_request()
        alpha = 1.0
        # Get expected returns using simulation.
        simulated = get_expected_utility(alpha, mean, sd)
        # Get expected returns using closed form.
        closed = np.exp(mean + (sd ** 2) * 0.5)
        # Assertions. Note the small number of decimal points
        # required. Given the precision of the Monte Carlo integration
        # this test if bound to fail sometimes.
        np.testing.assert_almost_equal(closed, simulated, decimal=3)



