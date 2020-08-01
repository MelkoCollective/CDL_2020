![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)



## Explain the technical problem you solved in this exercise
Simulated annealing is a probabilistic approach to determine the global optimum within large search spaces.  The inspiration for this originates from metallurgical annealing.  Annealing is the process of heating a metal and slowly lowering its temperature to decrease defects in the metal, which minimizes the energy of the system. The temperature will incrementally decline from an initial positive value to zero. The algorithm will randomly choose a solution close to the current solution and measures the viability before moving to that solution. 

## Explain or provide examples of the types of real-world problems this solution can solve

Aircraft Fleet Assignment:
>The assignment of the right aircraft types to the correct flights to make the maximum profits for airlines is a critical part of the airline production schedule and organization. Through annealing we can create appropriate flight segments to optimize the resource utilization of airlines. 

Reactive Power Planning:
>Reactive power planning seeks to optimize the allocation of reactive power sources in a power system based on location and size. The goal of power planning is to minimize the cost of new power supplies. 

Generator Maintenance Scheduling and Unit Commitment:
>Generators require a maintenance schedule that is critical to their economics and reliable operation. Preventative maintenance will prevent premature aging and the failure of generators in power systems. Unplanned and costly power outages are preventable by employing regular maintenance schedules.  Annealing can be a powerful tool when it comes to determining the optimal maintenance schedule for the machines. 

Finance:
>Monte Carlo simulation is a widely used technique in derivatives pricing. It generates a series of random variables that have similar properties that represent a large number of possible scenarios along with their probabilities. Although Monte Carlo simulation is used relatively rare for pricing the underlying (which is a stock price), it is the main tool to price index options (e.g. S&P500). Unlike single name options that are predominantly American and can be exercised at any time before the official expiration date, index options are mostly European style and can be exercised on an expiration date only. However, as almost any other method it has its drawbacks. The main disadvantage of MC simulation is that it is rather computationally expensive and slow if the number of scenarios is significantly large. I know the industry cases when that procedure can run through the whole night. Therefore any meaningful speedup would be highly beneficial for the financial industry. If I get it correctly, quantum algorithm can potentially provide a quadratic speedup for the Monte Carlo. Therefore, virtually all financial firms involved in the options trading would be desperate to become a client. Those firms can be divided in 2 groups: large investment banks and proprietary trading firms. Most prominent investment banks are Goldman Sachs, JP Morgan, Morgan Stanley, Citi Group, etc. They have huge resources but in the same time are relatively bureaucratic and I would not expect them to become the first customers. Proprietary trading companies include names like Optiver, IMC, Jump trading, Flow traders, etc. Those firms are relatively small but ultimately efficient in implementing novel technologies. As such, I would expect them to become the initial customers.

## Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Crew schedule planning is a periodic human resource planning ritual all airlines participate in to ensure their flights are assigned qualified and adequately rested pilots capable of safely operating the aircraft. 

Airlines generate flight schedules twice a year, one per season with transitions at daylight savings time to accommodate for seasonal demand and market adjustments.  

Trip Generation creates routes using the aircraft routing for assigning to pilots and flight attendants during the Trip Assignment process.  The complexity grows with an increasing number of aircraft. A small fleet comprised of one or two jetliners is handled manually. However, at a fleet size of 10, the problem begins to require automation and optimization becomes necessary.


## Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.
