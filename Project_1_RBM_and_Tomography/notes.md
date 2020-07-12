## Notes 

### Technical Team:
  - Andrew Patterson -- Training RBM models
  - Shumpei Kobayashi -- Training RBM models and MNIST models
  - Nick Allgood -- Additional dataset research, training, and analysis.

### Business Team:
  - Ramesh
  - Sheriff Ibrahim
  
## What we learned 

- Trained with RBM on 1000 epochs for only '0' shows improvement when compared to 100 epochs.
  -- Over time, initial states and sampling stems might be more important than epoch's

- We learned from MNIST training was that k of CD-k when sampling is important to produce accurate results when we have many visible nodes. It appears by chance we got 0.0001 with the initial k = 100. We needed k~O(v) when starting from random input where v = visibl nodes.

- It seemed by chance we were able to get 400 epoch of 400 hidden nodes within the first task. In the second task, the true configurations were almost 0.

- For the H2 case, 2visible - 10 hidden , which is estimated to be 100 ~ 500 visible. Good results were found under 100 hidden nodes, but the results weren't stable and seemed to be by chance. 

- For improvement, we might have to do a feed forward NN direction similar to say RNN, and it appears 0.0001 difference isn't quite reachable at this time.


## Additional Tasks 

### Dataset Info
- Using an additional dataset for solvated protein fragments: http://quantum-machine.org/datasets/

  **  Unke, O. T. and Meuwly, M. "PhysNet: A Neural Network for Predicting Energies, Forces, Dipole Moments and Partial Charges" arxiv:1902.08408 (2019). Unke, O.T. and Meuwly, M. (2019). Solvated protein fragments dataset. Zenodo. http://doi.org/10.5281/zenodo.2605372.

- This dataset probes many-body intermolecular interations between protein fragments and water moleculse -- both quite important to describe many condensed phase systems.

- Contains structures for all possible hydrogen-saturated covalently bonded fragments with up 8 heavy atoms: C, N, O, S

- These can be derived from chemical graphis of proteins containing 20 natural amino acids.

- All possible structures with a total charge of +-2e are included.

- Potential energy is given with respect to free atoms with the following constraints:

* H: -13.717939590030356 eV
* C: -1029.831662730747 eV
* N: -1485.40806126101 eV
* O: -2042.7920344362644 eV
* S: -10831.264715514206 eV

### Ideas and Objectives

- Original idea is to train x and y to the available energies provided by the data set.

- Another idea would take longer, but possibly training x and y to the dipole moment vector.

- We could also train x and y to vector containing the nuclear charges and atomic numbers of the nuclei.




  
