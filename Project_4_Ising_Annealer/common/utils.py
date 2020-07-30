import numpy as np


def exp_decay_schedule(N, Ti, Tf):
    """
    Construct a temperature sequence for exponential decay schedule
    
    Arguments:
        N: number of steps
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
        N: number of steps
        Ti: initial temperature
        Tf: final temperature
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    time = np.arange(N + 1)
    return Ti / (1 + (Ti / Tf - 1) * time / N), time


def poly_decay_schedule(N, Ti, Tf, degree):
    """
    Construct a temperature sequence for polynomial decay schedule given by a*x^degree + b
    
    Arguments:
        N: number of steps
        Ti: initial temperature
        Tf: final temperature
        degree: positive integer. The degree of the polynomial
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    time = np.arange(N + 1)
    return Ti + (Tf - Ti) * (time / N) **degree, time


def lin_decay_schedule(N, Ti, Tf):
    return poly_decay_schedule(N, Ti, Tf, degree=1)


def osc_decay_schedule(sched, time, a, b):
    """
    Add oscilations to an annealing schedule
    
    Arguments:
        sched: an annealing schedule
        time: the discrete time points of the schedule
        a: control the aplitude of oscillations
        b: control the number of oscillations 
        
    Returns:
        The sequence of temperature updates and the list of discrete time points
    """
    N = time.shape[0] - 1
    return sched * (a * np.sin(time / (N / b)) **2 + 1), time


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
