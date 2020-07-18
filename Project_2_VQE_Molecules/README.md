![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 2: VQE
This week you will explore the Variational Quantum Eigensolver (VQE) for
constructing potential energy surfaces for small molecules.
A very brief introduction to the main ideas behind the VQE are 
[here.](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/CDL_2020_docs.pdf)
Open up [Project2_LandingPage.pdf](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/Project_2_VQE_Molecules/Project_2_LandingPage.pdf)
to begin learning about your tasks for this week!

## Tasks and Challenges
Using H2 and H2O as examples, you will implement the main steps of the VQE process from the setup of the Hamiltonian to obtaining the circuit for the IBM quantum computer.  A number of additional challenges and 
business-related questions are suggested in the above.

## S1_Classical_Methods
We employ a variety of different classical algorithms for calculating the molecular bond energy. The choice of algorithm is based on a tradeoff between speed and accuracy. These methods give us an anchor to help us calibrate and understand our smaller scale quantum experiments.

## S2_Hamiltonian_gen
Generating the qubit hamiltonian requires mapping the fermonic states to qubit states through Jordan-Wigner transformation. The qubit hamiltonian produces the number of orbitals needed to represent the molecule and therefore the number of qubits required. We then tapper the hamiltonian to reduce the number of qubits required to represent the molecule. The elements of the tapered hamiltonian are then used to generate a matrix. The eigenvalues are then calculated from this matrix.

## S3_Unitary_Ansatz
We generate elementary unitary operations with UCC and QCC .Unitary Coupled Cluster seemed very resource heavy and took too long to generate any useful results. The Qubit Coupled Cluster was instead leveraged as it returned results within reasonable time frames. The calculations were done with STO-3G basis because the size of the calculations were reasonable and achievable with our available machines. 

## S4_Measurement
In MeasurementUnitaryGenerator.py we encapsulate all the functionality (partitioning into fully commuting groups and qubit-wise commuting groups) required for preparing the pre-measurement unitaries.
As a challenge, we also tried implementing further reduction via SVD truncation. We find that we are able to reconstruct the hamiltonian from the SVD, but we need to set high thresholds for truncation in order to get results similar to Table 1 of https://arxiv.org/pdf/2007.01234.pdf. For example, with H20, we need to set the threshold to ~50 in order to get a significant reduction (at this value we end up with 25 measurement groups after FC partitioning). To verify the resulting Hamiltonian, we computed its minimum eigenvalue (-82.4) and compared against that of the non-truncated version (-99.2). The energy difference seems large. We’d need further time to understand our method in detail and verify that we are applying the right steps.

## S5_Circuits

## Business Application
One again, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this solution can solve.
* Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)

## Presenting your results in your pull request
For your pull request, consider the following for the presentation of your final results:
- Work entirely in the directory for Project 2.
- Edit this README.md file with a highlight of your main technical results.  Provide links to any other files with your detailed results, e.g. Jupyter notebooks.
- For your Business Application, feel free to provide your answers directly in the 
[Business_Application.md](./Business_Application.md) file.
- Do not directly upload your video file (or any other large files) to the repository.  Instead, provide a link e.g. to a YouTube video, or a Google Drive file.
- Include a file contributions.md that lists the contributions of each group member.
