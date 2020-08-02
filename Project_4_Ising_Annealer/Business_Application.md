![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

The technical problem we solved in this exercise is to use thermal annealing to find the groundstate of a model. The model is important because we are mapping an electronic structure hamiltonian to a classical Ising model. Thermal annealing allows us exploit thermal fluctuations to escape local minimum. This mapping from scientific to business applications is due to the application of a probabilistic technique which helps us approxinate the global optimum of a given function.
The Monte Carlo simulation uses the Metropolis-Hastings algorithm for 2D ferromagnetic (J > 0) Ising model on a square lattice with periodic boundary conditions (PBCs).

We also investigate two 1D models - random bond nearest neighbor Ising model and a fully connected random bond Ising model, with the goal of analyzing different temperature decay schedules to figure out which works best. The comparisons were between the following : Exponential, Hyberbolic, Linear and Polynomial schedules. We also consider oscillating variations. The benchmarking of different schedules for different models is achieved using a hybrid scheduling, which is a mix of two parts including the hyperbolic, lowering the temperature rapidly and then transforming into linear until the end. The results are the conclusions that a new hybrid schedule works best for the nearest neighbor random model, and the exponential schedule works best for the fully connected model. This conclusion is then applied to the Mattis model, which is a fully connected Ising model.

We then consider the hydrogen molecule and show that its hamiltonian can be written in polynomial form, i.e. it can be mapped to an Ising model. Then this Ising model is used along with the software framework developed in previous tasks to find the ground state of the hydrogen molecule using simulated thermal annealing of the corresponding Ising model. As an additional challenge, we demonstrated that this 4-local hamiltonian can be converted into a 2-local hamiltonian (QUBO) by adding variables, and then this can be executed against the D-Wave machine. We validated the results of this approach and showed that they are in line with the other solution. 

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
Members can reserve vehicles with Zipcar's mobile app, online, or in some places by phone at any time, either immediately or up to a year in advance. Zipcar members have automated access to the cars using an access card which unlocks the door; the keys are already located inside. Alternatively, members can use Zipcar's Android or iPhone app to locate a Zipcar by honking its horn as well as to unlock the doors. Zipcar charges a one-time application fee, an annual fee, and a reservation charge. Fuel, parking, insurance, and maintenance are included in the price.

This solution will be useful for Zipcar because it can use it to plan the routes of its rental cars, including drop off and pickup locations to best optimize the entire route and lower the cost of the entire sequence of rides. It will be a combination of single travelling salesman problem, divided across multiple travelling salesmen.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

https://www.youtube.com/watch?v=dbeyh1pGVyE&feature=youtu.be
