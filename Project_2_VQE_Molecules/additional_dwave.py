#(Requires D-wave's Ocean SDK)
import neal
import dimod
import numpy as np
from dimod.core.polysampler import ComposedPolySampler, PolySampler
from dimod.higherorder.polynomial import BinaryPolynomial
from dimod.higherorder.utils import make_quadratic, poly_energies
from dimod.sampleset import SampleSet
from collections import defaultdict
import collections


#This code is directly taken from OCEAN SDK, Credit goes to them
def expand_initial_state(bqm, initial_state):
    """Determine the values for the initial state for a binary quadratic model
    generated from a higher order polynomial.

    Args:
        bqm (:obj:`.BinaryQuadraticModel`): a bqm object that contains
            its reduction info.

        initial_state (dict):
            An initial state for the higher order polynomial that generated the
            binary quadratic model.

    Returns:
        dict: A fully specified initial state.

    """
    # Developer note: this function relies heavily on assumptions about the
    # existance and structure of bqm.info['reduction']. We should consider
    # changing the way that the reduction information is passed.
    if not bqm.info['reduction']:
        return initial_state  # saves making a copy

    initial_state = dict(initial_state)  # so we can edit it in-place

    for (u, v), changes in bqm.info['reduction'].items():

        uv = changes['product']
        initial_state[uv] = initial_state[u] * initial_state[v]

        if 'auxiliary' in changes:
            # need to figure out the minimization from the initial_state
            aux = changes['auxiliary']

            en = (initial_state[u] * bqm.adj[aux].get(u, 0) +
                  initial_state[v] * bqm.adj[aux].get(v, 0) +
                  initial_state[uv] * bqm.adj[aux].get(uv, 0))

            initial_state[aux] = min(bqm.vartype.value, key=lambda val: en*val)

    return initial_state

#Taken from the neal package (D-wave)
def default_ising_beta_range(h, J):
    """Determine the starting and ending beta from h J
    Args:
        h (dict)
        J (dict)
    Assume each variable in J is also in h.
    We use the minimum bias to give a lower bound on the minimum energy gap, such at the
    final sweeps we are highly likely to settle into the current valley.
    """
    # Get nonzero, absolute biases
    abs_h = [abs(hh) for hh in h.values() if hh != 0]
    abs_J = [abs(jj) for jj in J.values() if jj != 0]
    abs_biases = abs_h + abs_J

    if not abs_biases:
        return [0.1, 1.0]

    # Rough approximation of min change in energy when flipping a qubit
    min_delta_energy = min(abs_biases)

    # Combine absolute biases by variable
    abs_bias_dict = defaultdict(int, {k: abs(v) for k, v in h.items()})
    for (k1, k2), v in J.items():
        abs_bias_dict[k1] += abs(v)
        abs_bias_dict[k2] += abs(v)

    # Find max change in energy when flipping a single qubit
    max_delta_energy = max(abs_bias_dict.values())

    # Selecting betas based on probability of flipping a qubit
    # Hot temp: We want to scale hot_beta so that for the most unlikely qubit flip, we get at least
    # 50% chance of flipping.(This means all other qubits will have > 50% chance of flipping
    # initially.) Most unlikely flip is when we go from a very low energy state to a high energy
    # state, thus we calculate hot_beta based on max_delta_energy.
    #   0.50 = exp(-hot_beta * max_delta_energy)
    #
    # Cold temp: Towards the end of the annealing schedule, we want to minimize the chance of
    # flipping. Don't want to be stuck between small energy tweaks. Hence, set cold_beta so that
    # at minimum energy change, the chance of flipping is set to 1%.
    #   0.01 = exp(-cold_beta * min_delta_energy)
    hot_beta = np.log(2) / max_delta_energy
    cold_beta = np.log(100) / min_delta_energy

    return [hot_beta, cold_beta]