import numpy as np

def exp_decay_schedule(N, T_i, T_f):
    t = np.arange(N+1)
    return T_i * ((T_f/T_i) ** (t/N)), t


def anneal(ising, schedule, mc_steps=1):
    for T in schedule:
        for _ in range(mc_steps):
            E = ising.mc_step(T)

    return ising.energy(), ising.spins
