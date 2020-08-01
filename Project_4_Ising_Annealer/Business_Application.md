![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

We have mapped an electronic structure hamiltonian to a classical Ising model, and then solved for the groundstate of the model using a thermal annealing Monte Carlo (MC) simulation. Thermal annealing is a probabilistic technique for approximating the global optimum of a given function by exploiting thermal fluctuations of the system under study. As for the Monte Carlo simulation, the Metropolis-Hastings (MH) algorithm is used. The Monte Carlo simulation employs MH algorithm for 2D ferromagnetic (J>0) Ising Model on square lattice with periodic boundary conditions (PBCs). The probability distribution of the Ising model at temperature T is given by the Gibbs distribution.The goal is to sample configurations from the distribution P. As the partition function requires exponential resources to compute, the MH algorithm is employed instead as approximation to original problem. The procedure is implemented using initial and final temperatures T=100 and T=0.01, respectively with exponentially decaying schedule. We then investigate two 1D models - random bond nearest neighbor ising model and a fully connected random bond Ising model where B = +1 or -1.Our main focus here is the analysis of different temperature decay schedules to find out which one works best. We have considered exponential, hyperbolic, linear and polynomial schedules, and oscillating variations thereof. 
To benchmark different schedules for different models, we also considered a hybrid scheduling, which is a mix of two parts - hyperbolic, lowering the temperature rapidly, then transforming into linear until the end. The blue and black curves in the figure are the hyperbolic and the exponential schedules. The analysis shows that a new hybrid schedule works best for the nearest neighbor random model, and the exponential schedule works best for the fully connected model. Finally, we apply the obtained knowledge to a particular model of fully connected ising model, which is the Mattis model. We then consider the hydrogen molecule and show that its hamiltonian can be written in polynomial form, i.e. it can be mapped to an ising model. Then this Ising model is used along with the software framework developed in previous tasks to find the ground state of the hydrogen molecule using simulated thermal annealing of the corresponding ising model. As an additional challenge, we demonstrated that this 4-local hamiltonian can be converted into a 2-local hamiltonian (QUBO) by adding variables, and then this can be executed against the Dwave machine. We validate the results of this approach and show that they are in line with the other solution. 

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

This solution can solve any real world problem that is based on the travelling salesman problem. Some common applicable uses are :

1) Routing signals in electronics to minimize cross-talk
2) Distributing ﬁnancial portfolios to maximize proﬁt while minimizing risk
3) Identifying the most likely nexus within a dense network of telephone calls
4) Identifying the best pick up and drop off locations for care rental service
5) Routing robotic applications on a factory floor
6) Fleet routing including school bus and airlines
7) Planning for delivery services

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Zipcar is an American car-sharing company and a subsidiary of Avis Budget Group. Zipcar provides automobile reservations to its members, billable by the minute, hour or day; members may have to pay a monthly or annual membership fee in addition to car reservations charges. Zipcar was founded in 2000 by Antje Danielson and Robin Chase.
Members can reserve vehicles with Zipcar's mobile app, online, or in some places by phone at any time, either immediately or up to a year in advance. Zipcar members have automated access to the cars using an access card which unlocks the door; the keys are already located inside. Alternatively, members can use Zipcar's Android or iPhone app to locate a Zipcar by honking its horn as well as to unlock the doors.Zipcar charges a one-time application fee, an annual fee, and a reservation charge. Fuel, parking, insurance, and maintenance are included in the price.

This solution will be useful for Zipcar because it can use it to plan the routes of its rental cars, including drop off and pickup locations to best optimize the entire route and lower the cost of the entire sequence of rides. It will be a combination of single travelling salesman problem, divided across multiple travelling salesmen.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.
