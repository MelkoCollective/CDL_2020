![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 4: Ising Annealing

This final project guides through the process of mapping an electronic structure Hamiltonian to a classical Ising model, and then solving for the groundstate of the model using a thermal anneling Monte Carlo (MC) simulation. This is yet another method as opposed to the other methods used in the first two projects that used RBMs and VQE, respectively.
The strategy of this project is to map the electronic structure Hamiltonian problem to a clasical problem, then to use methods such as Monte Carlo simulation to implement _thermal annealing_. Thermal annealing is a probabilistic technique for approximating the global optimum of a given function by exploiting thermal fluctuations of the system under study. As for the Monte Carlo simulation, the Metropolis-Hastings (MH) algorithm is used.
For very brief introduction to the main ideas behind the project, and the basics of the Monte Carlo method are summarized
[here.](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/CDL_2020_docs.pdf)  
And in the [Project 4 Landing Page](./Project4_LandingPage.pdf),a more technical information on the Ising Hamiltonians is provided.

## Tasks:
**Task 1:** In this task we are given a solution to an MC simulation that employs MH algorithm for 2D ferromagnetic (J>0) Ising Model on square lattice with periodic boundary conditions (PBCs).  
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=H=-J\sum_{<i,j>}\sigma_i\sigma_j" width="200">  
</p>
The probability distribution of the Ising model at temperature T is given by the Gibbs distribution:  

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(\sigma,T)=\frac{1}{Z(T)}\exp{\Big(-\frac{H(\sigma)}{T}\Big)}," width="200">
</p>  
where Z(T) is the normalization constant (also known as the partition function), <img src="https://render.githubusercontent.com/render/math?math=\sigma" > describes one of (exponentially) many possible microscopic configurations that the system can be in, H is the corresponding energy (Hamiltonian). So the goal is to sample configurations from the distribution P. As the partition function requires exponential resources to compute, the MH algorithm is employes instead as approximation to original problem. In [Task 1 jupyter notebook](./Task_1.ipynb) the procedure is implemented using initial and final temperatures T=100 and T=0.01, respectively with exponentially decaying schedule 
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=T(t)=T_{\text{init}}\Big(\frac{T_{\text{fin}}}{T_{\text{init}}}\Big)^{t/N} \hspace{1cm} t=[0,1,2,\ldots, N]" width="400">
</p> 
The notebook contains the object `Ising2DPBC` which creates an instance of an ising model by specifying the 2D grid and the parameter J. This object can compute the energy for the specified system and the energy difference that results from flipping one of the sites in the grid. The object `Ising2DPBC` inherits from the `AbstractIsing` parent class implemented in the `common/abstract_ining.py` file which also performs the Monte-Carlo step using Metropolis-Hastings algorithm.  
Another nice feature is implemented in the `common/ising_animator.py` file.  

* Perform thermal annealing to solve for the groundstate of a ferromagnetic Ising model.
* Perform thermal annealing to solve for the groundstate of disordered Ising models.
* Apply what you have learned to solve the Hydrogen molecule groundstate.

TODO: save at least one animation as gif, and put it here in readme.

**Task 2:** In this task we investigate two 1D model - random bond nearest neighbor ising model and a fully connected mode. Our main focus here is the analysis of different temperature decay schedules to find out which one works best. We have considered schedules of exponential, hyperbolic, linear and polynomial shapes, and oscillating variations of thereof. (TODO: add figure here). The analysis shows, that a new hybrid schedule works best for the nearest neighbor random model, and the exponential schedule works best for the fully connected model (TODO: figure?). Finally, we apply the obtained knowledge to a particular model of fully connected ising model, which is the Mattis model.

**Task 3:** In this task we look at the hydrogen molecule and show, that its hamiltonian can be written in polynomial form, i.e. it can be mapped to an ising model. (TODO: add something about 4-localness of this Hamiltonian). Then this ising model is used along with the software framework developed in previous tasks to find the ground state of the hydrogen molecule using simulated thermal annealing of the corresponding ising model. (TODO: figure and explanations). As an additional challenge, we also demonstrate, that this 4-local hamiltonian can be converted into a 2-local hamiltonian (QUBO) by adding variables, and then this can be executed against the Dwave machine. We validate the results of this approach and show that they are in line with the other solution. (TODO: figure here?)

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
