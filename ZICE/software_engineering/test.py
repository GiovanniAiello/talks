# standard library
import numpy as np

def get_expected_return(mean, sd):
    """ Get the expected returns by drawing numerous
    random deviates from a lognormal distribution.
    """
    # Guard interface
    assert (isinstance(mean, float))
    assert (isinstance(sd, float))
    assert (sd >= 0.00)
    
    # Set parametrization for Monte Carlo 
    # integration.
    num_draws = 10000
    
    # Draw ten-thousand deviates from the 
    deviates = get_random_deviates(mean, sd, num_draws)
    
    # Calculate the average from all deviates.
    rslt = np.mean(deviates)
    
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
    # Draw random deviates from a normal 
    # distribution.
    deviates = np.random.normal(size=2)
    
    # Split up the deviates and ensure 
    # that variance is nonnegative.
    mean, sd = deviates[0], 0.01 + 0.01
    
    # Finishing
    return mean, sd    


def test_random_requests():
    """ Draw a whole host of random requests to 
    ensure that the function works for all admissible 
    values.
    """    
    for _ in range(1000):    
        # Get expected returns.
        mean, sd = generate_random_request()
        get_expected_return(mean, sd)

def test_results():
    """ Test some previous knowledge about the results.
    """
    for _ in range(1000):    
        # Get expected returns.
        mean, sd = generate_random_request()
        rslt = get_expected_return(mean, sd)
        # Assertions
        assert rslt > 0   
        
def test_closed_form():
    """ Test the simulated result against the closed 
    form solution.
    """
    for _ in range(1):
        mean, sd = generate_random_request()
        # Get expected returns using simulation.
        simulated = get_expected_return(mean, sd)
        # Get expected returns using closed form.
        closed = np.exp(mean + (sd ** 2) * 0.5)
        # Assertions 
        np.testing.assert_almost_equal(closed, simulated)