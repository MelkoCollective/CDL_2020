![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Zzziiippp around the world with a Zipcar!

## Thermal Annealing as an Efficient Optimization procedure

The technical problem we solved in this exercise is to use thermal annealing to find the groundstate of a model. The model is important because we are mapping an electronic structure hamiltonian to a classical Ising model. Thermal annealing allows us exploit thermal fluctuations to escape local minimum. This mapping from scientific to business applications is due to the application of a probabilistic technique which helps us approxinate the global optimum of a given function.
The Monte Carlo simulation uses the Metropolis-Hastings algorithm for 2D ferromagnetic (J > 0) Ising model on a square lattice with periodic boundary conditions (PBCs).

We also investigate two 1D models - random bond nearest neighbor Ising model and a fully connected random bond Ising model, with the goal of analyzing different temperature decay schedules to figure out which works best. The comparisons were between the following: Exponential, Hyberbolic, Linear and Polynomial schedules. We also consider oscillating variations. The benchmarking of different schedules for different models is achieved using a hybrid scheduling, which is a mix of two parts including the hyperbolic, lowering the temperature rapidly and then transforming into linear until the end. The results are the conclusions that a new hybrid schedule works best for the nearest neighbor random model, and the exponential schedule works best for the fully connected model. This conclusion is then applied to the Mattis model, which is a fully connected Ising model.

We then consider the hydrogen molecule and show that its hamiltonian can be written in polynomial form, i.e. it can be mapped to an Ising model. Then this Ising model is used along with the software framework developed in previous tasks to find the ground state of the hydrogen molecule using simulated thermal annealing of the corresponding Ising model. As an additional challenge, we demonstrated that this 4-local hamiltonian can be converted into a 2-local hamiltonian (QUBO) by adding variables, and then this can be executed against the D-Wave machine. We validated the results of this approach and showed that they are in line with the other solution. 

## Examples of real-world problems that can benefit from Thermal Annealing as an Efficient Optimization procedure

Everyday Problems, where there is an exponential increase in the number of possibilities due to their combinatorial nature, are well-suited for Thermal Annealing.
The method can solve any real-world problem that is based on the traveling salesman problem. Some common applicable uses are:

1) Routing signals in electronics to minimize cross-talk;
2) Distributing ﬁnancial portfolios to maximize proﬁt while minimizing risk;
3) Identifying the most likely nexus within a dense network of telephone calls;
4) Identifying the best pick up and drop off locations for car rental service;
5) Routing robotic applications on a factory floor;
6) Fleet routing including school bus and airlines;
7) Planning for delivery services;

## Why Zipcar could be a great partner and how Thermal Annealing can help

Zipcar is an American car-sharing company and a subsidiary of Avis Budget Group. Zipcar provides automobile reservations to its members, billable by the minute, hour or day; members may have to pay a monthly or annual membership fee in addition to car reservations charges. Zipcar was founded in 2000 by Antje Danielson and Robin Chase.
Members can reserve vehicles with Zipcar's mobile app, online, or in some places by phone at any time, either immediately or up to a year in advance. Zipcar members have automated access to the cars using an access card which unlocks the door; the keys are already located inside. Alternatively, members can use Zipcar's Android or iPhone app to locate a Zipcar by honking its horn as well as to unlock the doors. Zipcar charges a one-time application fee, an annual fee, and a reservation charge. Fuel, parking, insurance, and maintenance are included in the price.

We are proposing a new service for Zipcar for budget travel from one city to another. This may be usefull for people who need to get to another city, but are not concerned with exact date when this is going to happen. First, many people need to request a car to travel from one city to another. Then, Traveling Salesman Problem can be used to model this where a single car is represented by salesman and a desired trip from city to city is represented by a single directional edge between two nodes. This way the car travels between cities changing drivers in every city. A basic implementation of Traveling Salesman Problem can be found here [TSP.ipynb](TSP.ipynb). A futher improvements to the solution in this jupyter notebook can be done by making graph single directional, removing requirement to return to the original city and changing the model to multiple salesman (cars) problem.

## Below is a 90 second video explaining the value proposition of our innovation

https://www.youtube.com/watch?v=dbeyh1pGVyE&feature=youtu.be
