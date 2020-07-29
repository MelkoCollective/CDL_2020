import numpy as np

def exp_decay_schedule(N, T_i, T_f):
    """
    Construct a sequence of exponential temperature decay schedule
    
    Arguments:
        N: number of discrete time points
        T_i: initial temperature
        T_f: final temperature
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    t = np.arange(N+1)
    return T_i * ((T_f/T_i) ** (t/N)), t


def anneal(ising, schedule, mc_steps=1):
    """
    Run simulated annealing
    
    Arguments:
        ising: an ising model
        schedule: temperature decreasing schedule
        mc_steps: number of mc steps to do at each temperature
    
    Returns:
        The final energy value found adn the corresponding spin configuration
    """
    for T in schedule:
        for _ in range(mc_steps):
            E = ising.mc_step(T)

    return ising.energy(), ising.spins
