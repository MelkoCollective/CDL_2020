## Project 1: Machine Learning

Please see **Week_1.ipynb** for the details of the models and results.

We trained several RBM models that were meant to capture the statistical behaviour of the quantum state of a molecule. 

The trained RBM models gives compact representations that mimic the state with fewer parameters. For the case of the Rydberg atom for instance, the quantum state involved 100 qubits which gives 2^100 complex parameters. But the RBM alternative has only a few hundreds parameters and is much easier to work with. 

Note that this is a fully classical computation. In some sense, we are using classical machine learning techniques to help quantum computation. 

This could be potentially helpful for validation and benchmarking the outcomes of a quantum computer or a quantum simulator that tries to solve problems in Quantum Chemistry. 

For NISQ devices, since error correction and FT is not available yet, we would need metrics to make sure that the quantum output is relevant. 

One approach would be that we train an RBM that mimics the state from the experimental data on the molecule and then compare it to the result of the quanutm computer or quantum simulator. 

This could be potentially interesting for companies like IBMQ and Google that aim at solveing quantum Chemistry problems using their NISQ devices. 

For the 90 sec. video, plese follow this link:

https://drive.google.com/drive/folders/1nyog3QDPF9_2ES5k6dIMDEVECFrid3Ir?usp=sharing
