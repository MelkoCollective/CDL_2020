from sklearn.linear_model import LinearRegression
import numpy as np
import tequila as tq
from typing import Union


class NoiseMitigation:

    def __init__(self, backend: str = 'qiskit', noise_model: tq.NoiseModel = None, device: str = None):
        self.backend = backend
        self.noise_model = noise_model
        self.device = device

    @staticmethod
    def noisy_iden(a, b):
        op = tq.gates.CX(a, b)
        op += tq.gates.CX(b, a)
        return op

    @staticmethod
    def noise_on_qubits(qubits: list):
        return [NoiseMitigation.noisy_iden(i, j) for i, j in zip(qubits, [qubits[-1]] + qubits[:-1])]

    @staticmethod
    def make_noisy(circ: tq.QCircuit):
        noisy_ops = NoiseMitigation.noise_on_qubits(circ.qubits)
        n_noisy_ops = len(noisy_ops)
        for i, moment in reversed(list(enumerate(circ.moments))):
            circ = circ.insert_gates([i + j for j in range(n_noisy_ops)], noisy_ops)
        return circ

    def zero_noise_expansion(self, H: tq.QubitHamiltonian, U: tq.QCircuit, variables: dict, samples: int = None):
        E = tq.ExpectationValue(H=H, U=U)
        low_noise = tq.simulate(E, variables=variables, backend=self.backend, device=self.device, samples=samples)
        noisy_U = NoiseMitigation.make_noisy(U)
        noisy_E = tq.ExpectationValue(H=H, U=noisy_U)
        noisy = tq.simulate(noisy_E, variables=variables, backend=self.backend, device=self.device, samples=samples)
        x1 = U.canonical_depth
        x2 = noisy_U.canonical_depth
        zero_n = NoiseMitigation.linear_fit([x1, x2], [low_noise, noisy])
        return zero_n, low_noise

    @staticmethod
    def linear_fit(xs: Union[np.ndarray, list], ys: Union[np.ndarray, list]):
        xs = np.array(xs).reshape((-1, 1))
        ys = np.array(ys)
        model = LinearRegression()
        model.fit(xs, ys)
        zero_n = model.predict(np.array([0]).reshape(1, -1))
        return zero_n[0]


if __name__ == '__main__':
    from utility import *
    x1 = 30
    x2 = 60
    y1 = 0.5
    y2 = 1
    print(NoiseMitigation.linear_fit([x1, x2], [y1, y2]))






