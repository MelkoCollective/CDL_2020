![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)

# Quantum Cohort Project Business Application

This week our team explores the Variational Quantum Eigensolver (VQE) for constructing potential energy surfaces for small molecules. Our main goal in the project was to illustrate main steps of the VQEframework using small molecules of increasing computational difficulty. In addition, we want to compare classical technoques of creating VQE algorithms.

## Q&A #1: What is the purpose of the analysis here?

The analysis conducted here is the performance investigation of the variational quantum eigensolver (VQE) as a variational quantum algorithm dedicated to the simulation of molecules. What we want to check is if the results provided by the algorithms do yield same or better (in the sense of more accurate) results than classical computation for small molecules. This analysis will allow us to specify if this algorithm could demonstrate a significant and reliable advantage for simulations of larger molecules which are not tractable by classical computation due to the amount of data that has to be processed.


## Q&A #2: How do the VQE and QAOA methods provide an advantage over classical machine learning methods?

VQE & QAOA are both constituents of a class of  algorithms that are called variational quantum algorithms. The interest of these kind of methods is to use simultaneously the power of the quantum computer and the flexibility of classical computation in order to handle problem instances of  sheer sizes (in terms of the data that has to be handled). The advantage over classical methods could come from the fact that, under the assumption that these methods do same or better quality of results on datasets that are handled well by classical computers today, they would be able to handle much more problem instances that are intractable due to the curse of dimensionality associated to the data that has to be dealt with.

## Q&A #3: How do these methods help in discovering new molecules?

By simulating at the lowest scale (electrons, nuclei, etc…) the molecular structure, one can develop a set of tools allowing us to determine a set of useful properties associated to certain compounds or materials. Typically, one could imagine to find high temperature superconductivity by identifying new set of alloys that couldn’t be imagined by the usual experimental research. The ability to play on the ground structure of the molecules allows the reconstruction of all kinds of different macroscopic properties, the same reasoning might apply for active principle in a chemical compound for the design of drugs.

## Q&A #4: Is there a possibility assess therapeutic properties of these molecules i.e how do they get absorbed into the human body, how can they target specific cells or pathogens in the body.


The idea is that, when having the full simulation of the molecules at hand, one could try to also simulate the reaction of such molecule under different external conditions (aka pressure, temperature, viscosity, etc…). Therefore, it would take a lot more work to be able to transform this external information into an input of the quantum computer, but one could imagine that once such mappings are achieved, we might encounter all sorts of possible scenarios for different molecules. What is therefore remaining is the investigation of all the possible scenarios and picking the one yielding satisfactory results.

## Q&A #5: Also, is it possible to evaluate physical properties of these molecules computationally rather than creating them. How can we create these molecules in real life. i.e even if they are computationally possible are there physical constraints to reach the energy states required for the creation of these new molecules?

As it was suggested before, physical properties of materials are at the core of what we want to investigate with this kind of algorithm. Creating these molecules in real life is another challenge not anymore related to its simulation but to the feasibility of the simulated scenario. 
