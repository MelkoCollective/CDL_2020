![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

### Business Application of Variational Quantum Eigensolver: Constructing Potential Energy Surfaces for Small Molecules Group 4 (Week 2)

### Members

* Nick Allgood  
* Claudio Giampi'  
* Santanu Ganguly  
* Pooria Mandai

## Step 1: Explain the technical problem you solved in this exercise

In this project, we have tried to construct by using a general framework called VQE or Variational Quantum Eigensolver, and its optimization, the potential energy surfaces (PESs) or molecular energy, for the following molecules: H2, LiH, H4, H2O, N2. 
In our project, a sort of validated procedure was used in order to be applied for our samples on a classical computer using classical methods and by VQE simulator on a quantum computer. 

The project was split into 5 different steps.

* First step was to set the computer environment.
* Second step was to generate the molecular energy by using a classical method.
* Third step was to generate the Hamiltonian, which is the total energy of each individual system, in a qubit form.
* Fourth step was to transform the qubit Hamiltonian, generated in the third step, in unitary gates, in other words to create a circuit that can be measured.
* Fifth step was only the generation of the circuits by using compilers.

Once all steps were completed, it was possible to use the data generated in order to obtain the molecular energy of the molecules.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

In a scenario where it is feasible to obtain accurate PES of a molecule, this can be used to make predictions for example of how such energy is important in order to simulate chemical reactions. If in our case, we consider the PES of two separate molecules, e.g. H2 and N2, these can be used in order to study the chemical reaction 3H2 + N2 → 2NH3.

The above chemical reaction is one of the most important chemical reactions that we have today, which is used for Ammonia production and subsequently for fertilizers.
By knowing the energies implied in the two separate molecules H2 and N2, they can be used to study a more efficient way to produce Ammonia.
In fact, like every other chemical reaction, when 2 or more molecules come in contact with each other, there is some sort of probability, under certain condition, that the 2 or more molecules can be converted in a molecule different than the initial reactants, and 3H2 + N2 → 2NH3 is not an exception. 

The above chemical synthesis is feasible only under certain condition of appropriate temperature, pressure and/or catalyst.
In fact, by knowing the PES of the molecules, this can lead to a better understanding of how the energy can be used to study a more efficient catalyst that is able to act as a substrate where H2 and N2 can interact and be converted to Ammonia.The study of an efficient catalyst could be interesting from an environmental and energy consumption point of view. In fact, if further studies can be helpful to know what sort of energy is necessary to break the H2 and N2 bonds to allow Ammonia formation, the model could be used to determine the amount of energy required during the process and if the chemical reaction could be implemented. This would pave the way to energy reduction used during the synthesis. This is due to the fact that the chemical synthesis requires energy, or it requires heat, usually 400° - 500°C on an iron catalyst, to go to completion. By knowing the energy required, a formulation of a new catalyst or implementation of the old could be feasible, allowing as already mentioned energy reduction or process temperature reduced. 

In conclusion, by knowing the PES of our molecules H2 and N2 that we took into consideration, the formulation of a new catalyst that allows reduction of the energy used during the process could be feasible. However, reduction of the energy used during the process could also lead to CO2 reduction generated during the heat supply from an external source with a consequence of an impact on climate change. The above explanation is only in relation to one specific process.
However, knowing the PES of a molecule is very beneficial not only in understanding better chemical reactions but also in discovering new materials or new drugs for example and the chemistry involved in their synthesis.


## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

A potential customer that can use our solution to solve its problem, could be based in different sectors like pharmaceutical, petrochemical, and many others where their business value is originated from chemical reactions, for example.

In our case, we will take into consideration the already mentioned Ammonia production process or Haber – Bosch.

The process, as previously explained, involves a chemical reaction between H2 and N2 in order to produce NH3. However, the process can only be efficient if a catalyst would be used, and this catalyst is critical in the process because it allows to reduce the amount of energy required to break the H2 and N2 bonds, which allow NH3 formation. By knowing the PES of the two single molecules, it is possible to study a new catalyst or implement the old to make the process faster, then more time efficient. Obviously, a faster conversion rate means higher output, which is the business value that the solution offered could bring to the company using the process to produce Ammonia.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

https://drive.google.com/file/d/1u4UDkt0mHXaN97CHOXgMrbkwp_pl1ZO8/view?usp=sharing
