![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 4: Ising Annealing

Your final week's project will guide you through the process of mapping an electronic structure Hamiltonian to a classical Ising model, and then solving for the groundstate of the model using a thermal anneling Monte Carlo simulation.

A very brief introduction to the main ideas behind the project, and the basics of the Monte Carlo method are
[here.](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/CDL_2020_docs.pdf)

In our [Project4_LandingPage.pdf](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/Project_4_Ising_Annealer/Project4_LandingPage.pdf),
we provide more technical information the Ising Hamiltonians involved.
Click on this link to begin learning about your tasks for this week!

## Tasks include:
* Perform thermal annealing to solve for the groundstate of a ferromagnetic Ising model.
* Perform thermal annealing to solve for the groundstate of disordered Ising models.
* Apply what you have learned to solve the Hydrogen molecule groundstate.

## Further Challenges: 
* Explore the annealing procedure on the Mattis glass.
* Devise a 2-local Ising Hamiltonian for the Hydrogen molecule, and compare your results.
* Solve your 2-local Hamiltonian (or any Hamiltonian) on open-source commercial software, and compare the performance.
* Go wild and try thermal annealing on your favorite NP-hard problem!

## Business Application
One again, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this solution can solve.
* Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)

## Presenting your results in your pull request
For your pull request, consider the following for the presentation of your final results:
- Work entirely in the directory for Project 4.
- Edit this README.md file with a highlight of your main technical results.  Provide links to any other files with your detailed results, e.g. Jupyter notebooks.
- For your Business Application, feel free to provide your answers directly in the 
[Business_Application.md](./Business_Application.md) file.
- Do not directly upload your video file (or any other large files) to the repository.  Instead, provide a link e.g. to a YouTube video, or a Google Drive file.
- Include a file contributions.md that lists the contributions of each group member.


Task 3:
In the notebook [Task 3]('./Task_3.ipynb') we explore using Monte Carlo simulation to olve the Ising model as applied to
the Hydrogen molecule. This class has been written so that any dimension of Ising Hamiltonan can be passed to it, 
meaning that we can solve any classically tractable chemical Hamiltonian using this method. We have used Monte Carlo
sampling to  find the ground state energy and spin configuration for the Hydrogen molecule at a variety of bond 
distances This, wen applied to larger molcules is a useful input into commercial applications such as drug or catalyst
discovery.

Challenge 4:
In the [Challenge 4 notebook ]('./Challenge_4_Ising_Graph_Partition.ipynb') we have Hamiltonian which describes the 
graph partition problem. In yhe Graph partition problem we age given an input graph and asked to find two equally-sized
independent graphs. That means splitting the graph in to two equally sized sets of nodes with the fewest connections 
between the two subsets. THis is an extremely inportant problem to solve, as it splits hard intractable graph problems 
(such as the travelling salesman or Max-Cut) into two smaller problems which can be solved on classical or quantum
 hardware. For example, this calssical sub routine can be used to find graphs which fit onto current quantum hardware, 
 which would be otherwise unsolvable given the number of qubits currently available, allowing us to accelerate the time
 needed to solve graph problems leveraging quantum hardware.