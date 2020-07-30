import numpy as np


def exp_decay_schedule(N, Ti, Tf):
    """
    Construct a temperature sequence for exponential decay schedule
    
    Arguments:
        N: number of discrete time points
        Ti: initial temperature
        Tf: final temperature
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    time = np.arange(N + 1)
    return Ti * ((Tf/Ti) ** (time / N)), time


def inv_decay_schedule(N, Ti, Tf):
    """
    Construct a temperature sequence for hyperbolic decay schedule
    
    Arguments:
        N: number of discrete time points
        Ti: initial temperature
        Tf: final temperature
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    time = np.arange(N + 1)
    return Ti / (1 + (Ti / Tf - 1) * time / N), time


def lin_decay_schedule(N, Ti, Tf):
    """
    Construct a temperature sequence for linear decay schedule
    
    Arguments:
        N: number of discrete time points
        Ti: initial temperature
        Tf: final temperature
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    time = np.arange(N + 1)
    return Ti + (Tf - Ti) * time / N, time


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
