![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

We have used a powerful optimisation algorithm called simulated annealing to find optimal solutions to the Ising model [1]. The Ising model was developed to describe the interaction of a collection of quantum spins, but it can be used to model many other problems. As two examples, we tackled solving for the magnetisation in a certain class of materials called ferromagnets, and calculating the energy-landascape of the Hydrogen molecule as its being stretched. These problems are formulated in a quantum-inspired way, such that the software is easy to adapt to running on a quantum annealer instead of simulated annealing. Such powerful annealing devices are available from companies such as D-Wave [2] and Fujitsu [3]. 


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

The Ising model provides a model for machine learning and analysing neural networks [4,5,6]. With our powerful algorithms to solve the Ising model we can provide new tools into the machine-learning toolkit, particularly for giving insight into why a given input is mapped onto an output by the neural network [6]. The problem of why an AI algorithm based on neural networks makes a certain decison is a major hurdle preventing AI from being used in decision making by public and private entities in democratic systems. Thus analysis of the network that might provide insight into the decision making of the neural network is extremely valuable.


## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

There are at least two potential classes of customers:

### Governments
Various government agencies have tried using AI tools based on neural networks to increase efficiency in their operations. For example bail hearing have been adjudicated by AI [7], analysis of COVID-19 data for tracking [8], and smart robots usied for patrolling and surveillance [8]. These systems make decision regarding citizen's rights and must therefore be scrutinized and be explicable to the public for governments to be able to make widespread use of the technologies. The potential savings from replacing human decision making at lower levels provide the value the AI tools provide. Thus our analysis tool becomes highly valuable by enableing wide-spread use of AI.

### Regulated industries

Industries such as banking and insurance [9] have started using AI tools based on neural networks to make decisions regarding mortgages and insurance premiums. This has raised concerns about discrimination and lack of transparency of the decision making process [10]. Governemnts have laws and regulations that require equal treatment of customers, which in practice mean that any decisions taken must be explicable [11]. By using our tool based on the Ising-model these actors can gain new insight into the correlations between observables and use that to explain the decison made by the neural network. The enables banks and insurers to make wide-spread use of neural networks and achieve huge efficiency gains. These gains are estimated at 250B USD in both banking and insurance [12].
USD 

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.


###Referecens

[1] https://en.wikipedia.org/wiki/Ising_model
[2] https://www.dwavesys.com/
[3] https://www.fujitsu.com/global/services/business-services/digital-annealer/index.html
[4] https://www.pnas.org/content/79/8/2554
[5] https://link.springer.com/chapter/10.1007/978-3-642-61850-5_18
[6] https://arxiv.org/pdf/q-bio/0512013.pdf
[7] https://hbr.org/2018/01/how-ai-could-help-the-public-sector
[8] https://www.tech.gov.sg/media/technews/big-push-for-ai-proves-fruitful-and-useful
[9] https://emerj.com/ai-sector-overviews/artificial-intelligence-applications-lending-loan-management/
[10] https://www2.deloitte.com/us/en/pages/financial-services/articles/regulating-ai-in-the-banking-space.html
[11] https://qz.com/1277305/ai-for-lending-decisions-us-bank-regulations-make-that-tough/
[12] https://www.mckinsey.com/featured-insights/artificial-intelligence/notes-from-the-ai-frontier-applications-and-value-of-deep-learning#
