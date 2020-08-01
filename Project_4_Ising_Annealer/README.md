![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 4: Ising Annealing

This final project guides through the process of mapping an electronic structure Hamiltonian to a classical Ising model, and then solving for the groundstate of the model using a thermal anneling Monte Carlo (MC) simulation. This is yet another method as opposed to the other methods used in the first two projects that used RBMs and VQE, respectively.
The strategy of this project is to map the electronic structure Hamiltonian problem to a clasical problem, then to use methods such as Monte Carlo simulation to implement _thermal annealing_. Thermal annealing is a probabilistic technique for approximating the global optimum of a given function by exploiting thermal fluctuations of the system under study. As for the Monte Carlo simulation, the Metropolis-Hastings (MH) algorithm is used.
For very brief introduction to the main ideas behind the project, and the basics of the Monte Carlo method are summarized
[here.](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/CDL_2020_docs.pdf)  
And in the [Project 4 Landing Page](./Project4_LandingPage.pdf),a more technical information on the Ising Hamiltonians is provided.

## Tasks:
**Task 1: 2D ferromagnetic Ising Model**   
In this task we are given a solution to an MC simulation that employs MH algorithm for 2D ferromagnetic (J>0) Ising Model on square lattice with periodic boundary conditions (PBCs).  
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=H=-J\sum_{<i,j>}\sigma_i\sigma_j" width="200">  
</p>
The probability distribution of the Ising model at temperature T is given by the Gibbs distribution:   

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(\sigma,T)=\frac{1}{Z(T)}\exp{\Big(-\frac{H(\sigma)}{T}\Big)}," width="200">
</p>  

where Z(T) is the normalization constant (also known as the partition function), <img src="https://render.githubusercontent.com/render/math?math=\sigma" width="15"> describes one of (exponentially) many possible microscopic configurations that the system can be in, H is the corresponding energy (Hamiltonian). So the goal is to sample configurations from the distribution P. As the partition function requires exponential resources to compute, the MH algorithm is employes instead as approximation to original problem. 

In our [Task 1 jupyter notebook](./Task_1.ipynb) the procedure is implemented using initial and final temperatures T=100 and T=0.01, respectively with exponentially decaying schedule. 

The notebook contains the object `Ising2DPBC` which creates an instance of an ising model by specifying the 2D grid and the parameter J. This object can compute the energy for the specified system and the energy difference that results from flipping one of the sites in the grid. The object `Ising2DPBC` inherits from the `AbstractIsing` parent class implemented in the `common/abstract_ining.py` file which also performs the Monte-Carlo step using Metropolis-Hastings algorithm.  
Another nice feature is implemented in the `common/ising_animator.py` file. It creates an animation of the Ising Lattice simulation following the given annealing schedule. Here is an animation of the 2D Ising model:  

![animation](https://user-images.githubusercontent.com/25146937/89028323-2971a180-d33d-11ea-96af-d9e7f4bcf1e0.gif)
 


**Task 2: 1D random bond nearest neighbor, and random bond fully connected Ising models**   
In this task we investigate two 1D models - random bond nearest neighbor Ising model  

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=H=J\sum_{<i,j>}B_{ij}\sigma_i\sigma_j" width="200">
</p>  

 and a fully connected random bond Ising model

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=H=J\sum_{i<j}B_{ij}\sigma_i\sigma_j," width="200">
</p>   

where B = +1 or -1.  

 Our main focus here is the analysis of different temperature decay schedules to find out which one works best. We have considered **exponential**, **hyperbolic**, **linear** and **polynomial** schedules, and **oscillating variations** thereof. Below are the plots for the mentioned schedules: 

<p align="center">
<img src="media/schedules.png" width="400"/> <img src="media/oscil_schedules.png" width="400"/>
</p>

To benchmark different schedules for different models, we also considered a hybrid scheduling, which is a mix of two parts - hyperbolic, lowering the temperature rapidly, then transforming into linear until the end. The blue and black curves in the figure are the hyperbolic and the exponential schedules, presented for comparison.   

<p align="center">
<img src="media/hybrid_schedule.png" width="400"/>
</p>  

The analysis shows (see our [Task 2 jupyter notebook](./Task_2.ipynb) for details) that a new hybrid schedule works best for the nearest neighbor random model, and the exponential schedule works best for the fully connected model.   
(**Challenge 1**) Finally, we apply the obtained knowledge to a particular model of fully connected ising model, which is the Mattis model ("glass"). This challenge is implemented in the same jupyter notebook for Task 2. As expected, at the end of the annealing procedure we confirm that we've found the ground state by checking that 𝜉i is equal to  𝜎𝑖  up to a global sign, i.e. if we multiply the spin configuration elementwise with 𝜉, we will get all 1s, or all -1s.

**Task 3: Electronic Structure Calculations using Generalized Ising Hamiltonians**   
In this task we look at the hydrogen molecule and show, that its hamiltonian can be written in polynomial form, i.e. as a generalized Ising model. Then this Ising model is used along with the software framework developed in previous tasks to find the ground state of the Hydrogen molecule using simulated thermal annealing of the corresponding Ising model. 

<p align="center">
<img src="./media/mc_and_exact.png" width="400"/>  <img src="./media/energies_comparison.png" width="400"/>
</p>

The left figure above shows the energies (exact and from simulated annealing results for the generalized Ising model) for different bond distances for Hydrogen molecule. The data for loading into our generalized Ising model are provided in the `./hamiltonians` folder (it would be good to have more data corresponding to smaller bond distances to see the familiar full curve and not only the minimum and the right part). As we can see there is a good correspondence.  

(**Challenges 2 and 3**)   
The right figure above is the comparison between:  
- the exact model for full generalized 4-body Ising model,
- the model run on the Dwave's commercial software,
- and the `GeneralizedIsingModel` devised in this task.   

For the last two cases we have used the function `poly_to_quadratic` function implemented using `dimod.make_quadratic`(**Challenge 2)**.   
As can be seen they are all in line with the other solutions.  
See more details on the code implementations and demos in our [Task 3 jupyter notebook](./Task_3.ipynb).

## Further Challenges: 
* Go wild and try thermal annealing on your favorite NP-hard problem!

## Business Application
We provide examples of real-world problems our solutions in above tasks can solve. We then identify a potential customer for this solutions. We also prepare a short video explaining the value proposition of our innovation to this potential customer in non-technical language.  
For more details refer to our [Business Application file](./Business_Application.md)

(TODO) Include a file contributions.md that lists the contributions of each group member.
