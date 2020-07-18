![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

<Pravin, Mario - please add any context if you can, thanks!>

High-level problem: Using VQE to obtain potential energy surfaces (PSEs) for small molecules.

1. We employ a variety of different classical algorithms for calculating the molecular bond energy. The choice of algorithm is based on a tradeoff between speed and accuracy. These methods give us an anchor to help us calibrate and understand our smaller scale quantum experiments.

4. Measuring the outcome of each trial run actually requires a large number of physical measurements because quantum hardware can only measure the system in one quantum dimension at a time. We use novel techniques to reduce the number of measurements required, by grouping components of the quantum system together into configurations which require only one measurement for the whole group. By forming these groups, we can reduce the number of measurements required by factors of 3 to several 100. Again, the tradeoff is between speed and accuracy. Coarser grouping reduces accuracy but results in less measurements.


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

We know about one main problem/use case from our readings:

Use Case: An R&D scientist is trying to understand the potential energy surfaces (PSE) of molecules so that he can develop better pharmaceutical drugs.

Problem: Finding the lowest energy state of a molecular Hamiltonian cannot be solved exactly for more than a few atoms. For large molecules this problem is intractable even on today's largest supercomputers.

In addition to this understanding, our team decided to conduct primary interviews with QC companies who interact with customers on a daily basis. To that end, we set up calls with experts at IBM and Zapata.

Gavin Jones, Team Lead, Quantum Applications, IBM (PhD Chemistry, UCLA)

Pain points

This was a very insightful call with Gavin. I started off by asking him generally about customer articulated pain points within chemistry/pharma. Gavin said that people in industry aren’t very interested in the latest research, e.g. PES bond stretching. Yes, they may be interested in PES from a benchmarking standpoint, but they want to focus on applications that industry cares about. They want to better understand 2-3 molecule reactions. One area of interest are catalysts performing reactions with one molecule and then another, thereby accelerating the union of those two molecules. Also, can we rearrange reactions?

Areas of interest outside of PSE

Outside of reactions, another area of interest are general properties of molecules. Examples include dipole moments, excited states (this is one property, he says, that all industries care about!), electro-chemical processes - Can we make OLEDs, photoacid generators, and better batteries out of these things? Scientists also care about the interaction of molecules with light. On the materials side, they care about periodic solids and crystalline materials. And, one thing scientists care about that is cross-cutting is quantum machine learning to improve anything that they are doing classically. 
I asked him how receptive the business side is to quantum experimentation. He said that they are in very early stages, so it is still very scientist driven. He said that they still have to be convinced that they need to be ready for a quantum future. But, he said that one thing that surprised him is that there is quite a bit of C-level interest in quantum. He believes that one reason that they are excited is because they realize that they don’t have to invest that much to get started (i.e. they don’t have to build a quantum computer themselves). Also, sometimes C-level executives are interested in areas outside of simulation, like optimization. CEOs are asking their teams to look into the benefits of quantum computing. 

Great anecdote

I asked Gavin if he knows of cases where VQE has been used in industries outside of chemistry/pharmaceuticals. He said that VQE has actually been adapted and used in finance for the use case of CVAR (conditional value-at-risk). Then they took this method from finance and used it back in the chemistry world!
Also he said people have thought about how to use VQE QAOA for optimization algorithms within chemistry. 

Large molecules

I asked Gavin if there large molecules that currently cannot be studied, but that are very important/impactful. His immediate answer was the iron complex that is used for nitrogen fixation (1-2% of the world’s energy is consumed for this process). But he said we are probably years away from fully understanding that. 

Personal excitement

Gavin would love to see the day where quantum computers are used routinely in chemistry. He remembers roles that he had where he was modeling different materials and reactions. He never knew how believable his results were, and the methods could be quite wrong. He said that sometimes he didn’t have time for benchmarking. So, he would have to go back to experimentalists in the lab to verify his results. He’s excited about having more accurate methods. 
I asked him what’s the impact of something that’s not so accurate. He gave an example of trying to design a new catalyst. Experimentalists may come to him with a problem - we have seen X happening and we don’t know why. Then he would try to model the problem on a classical computer. They try your results in the lab, and it’s quite embarrassing if it does not work! If it was more accurate you could help them improve yields for desired products, reaction rates. 

James Ma, Product Manager, Zapata (Computer Science background)

James isn’t a chemistry expert, so he didn’t have much to say about the technical components of VQE, molecules etc. But, he did mention that quantum advantage hasn’t been proven in VQE so the benefits to customers is an open question, Here are some highlights from our conversation:

Hedging: The first is what is already commonly known - We haven’t been able to simulate something or access research because of the limits of classical computing. We can't execute algorithms in a reasonable amount of time. So we view this as a hedge since this is an active area of research. It’s on us to allocate resources to this.  

Software best practices 101: The more interesting finding is that these groups have basic problems related to software engineering principles and practices that are really stifling their progress. One example is that we have seen that they email code around instead of using repositories on Github! They don’t use microservices. One big problem is reproducibility of code - if someone develops something and leaves, they have a lot of loss related to that. We help our clients with these basics and they really appreciate it; it creates stickiness for us. 
Shift from algorithms to tooling: Generally James sees a shift from a focus on algorithms to tooling. Scientists need to build the capabilities to access quantum computing, and we are creating that new abstraction level. We want the barrier to using quantum computing to be lower. 

Quantum inspired: Clients are exploring the area of quantum inspired algorithms. They want to know if exploring quantum can help them improve their classical methods. 

Costs: Executives want to cut costs, but they don’t care if it comes from AI, blockchain or quantum. But, James believes that the cost advantages from quantum come from increased reliability, less asynchronous computing, and time savings. 

Four levels of customers:

1. Proof of concept: These customers don’t really get quantum yet, so they want to have workshops and learn and perhaps design initial experiments or collaborations
2. Resource estimation: These clients understand the benefits of quantum computing. They want to know about resource estimation - how many qubits do we need and what stability do we need before I need to care/invest in this?
3. Workflow: How do I implement quantum and integrate it into my existing workflow pipeline? How do I productize it?
4. Novel IP: We want to develop the quantum version of X algorithm before anyone else, or maybe it’s something specific to a chemical they are developing. They want patents. 

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Executive summary: We would initially focus on pharmaceutical companies and maybe the top two chemicals companies (Dupont, BASF). For pharma companies, we would focus on companies who have shown significant quantum interest. This list seems pretty short though (Merck, Abbvie, Bayer, Novartis). We would also cast a wider net (i.e. look at pharma firms beyond the top 10) and take a more educational/workshop (increase awareness) approach as a “foot-in-the-door” strategy. 

We are going to target the pharmaceutical industry. Below you see a chart of the revenue rankings for pharmaceutical companies in 2020. For these firms, we also want to understand if they are already interested/investing in quantum computing. The idea is that if they are already interested/investing, then they will be more receptive to our pitch. 

Source: https://www.bizvibe.com/blog/largest-pharmaceutical-companies/

Here is the evidence that we found that these 10 firms are quantum interested:

Johnson & Johnson
Supply chain executive believes quantum can have an impact in the next few years
https://www.cxotalk.com/video/johnson-johnson-creates-intelligent-supply-chain
Neil Ackerman, Global Supply Chain Digital Executive: 
https://www.linkedin.com/in/neilackerman/

Roche
Found a number of articles, social media posts:
https://www.roche.com/quantum-computing.htm
https://www.roche.com/future-quantum-computing.htm

Martin Strahm,Head of Data Science: 
https://www.linkedin.com/in/martin-strahm-56a67b12a/
https://www.facebook.com/RocheCareers/posts/2458483347511552

Pfizer
Some evidence that Pfizer has partnerships with AI companies that are experimenting with quantum computing:
https://www.breakthroughs.com/health-tomorrow/how-quantum-physics-and-ai-disrupting-drug-discovery-development

Bruno Hancock, Global Head of Materials Science: 
https://www.linkedin.com/in/bruno-hancock-20a3b210/
https://pharmaphorum.com/news/pfizer-ai-drug-discovery-xtalpi/

Bayer
Bayer is hiring for the role, Quantum Computing Manager. The posting says that Bayer has been working on quantum since 2016. 
https://career.bayer.us/en/job/quantum-computing-manager--SF142341
This article mentions that in 2018, Bayer was working with Atos to explore quantum computing applications for human disease patterns:
https://atos.net/en/2018/press-release_2018_11_07/atos-bayer-rwth-aachen-university-use-atos-quantum-learning-machine-study-human-disease-patterns
Ulf Hengstmann, IT Manager: 
https://www.linkedin.com/in/ulf-hengstmann-bbb479/

Novartis
They have an existing partnership with Microsoft that they would like to expand. This may include quantum computing. 
Forbes article mentions that new CEO is keen on using quantum computing
https://www.forbes.com/sites/matthewherper/2018/03/26/ai-telemedicine-quantum-new-novartis-boss-says-tech-will-finally-change-the-drug-biz/#308a58656b54

Merck
Earlier this year, Merck’s venture arm invested in a quantum startup, Seeqc:
https://www.wsj.com/articles/merck-venture-arm-invests-in-quantum-computing-startup-seeqc-11586454285
Announcement of partnership with HQS Quantum Simulations, a quantum startup:
https://www.emdgroup.com/en/news/quantum-computing-04-06-2019.html
Philip Harbach, Head of In Silico Research: https://www.linkedin.com/in/philipp-harbach-579670172/
Kam Chana, Director Computational Platforms, attended a quantum conference (QTech) in Boston last September.
https://www.linkedin.com/in/kam-chana/

GlaxoSmithKline
GSK has invested in a company called Cloud Pharmaceuticals that is exploring quantum applications:
https://www.biopharmatrend.com/post/99-8-startups-applying-quantum-calculations-for-drug-discovery/
It looks like GSK has partnered with industry groups to explore quantum:
https://quantumlab.info/2019-1
https://admin.ktn-uk.co.uk/app/uploads/2019/04/QC_Pharma_140319.pdf
https://gtr.ukri.org/projects?ref=EP%2FT001062%2F1
Potential lead - Bonnie Kruft, Director of Data Science:
https://www.linkedin.com/in/bonniekruft/?originalSubdomain=uk

Sanofi
Did not find any evidence of quantum interest/investment

AbbVie
Brian Martin, Head of AI in R&D Information Research: 
https://www.linkedin.com/in/brianm1028/
Tweet: https://twitter.com/abbvie/status/1228695498191757312

Brian attends several quantum conferences
https://www.quantumtechcongress.com/agenda/conference-day-one
https://www.bio-itworld.com/2020/02/11/abbvies-fresh-look-at-how-ai-and-quantum-computing-will-transform-biotech.aspx

Abbott
Did not find any evidence of quantum interest/investment

Largest chemical companies by sales - here we would approach the top two, DuPont and BASF, and then expand beyond these two. 

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Many of our clients in the chemicals and pharmaceutical industry are interested and have invested in quantum computing for several reasons:
 
Simulation: There is a potential to learn about molecules in a way that simply isn’t possible on classical computers. These learnings, for example with catalysts, can help scientists speed up chemical reactions and yields for specific products. This will have revenue-side benefits for organizations. 

Machine learning/Optimization: Outside of molecular simulation, clients also care about how QC can help with optimization, and accelerate machine learning. 

Learning curve: While perfect quantum hardware does not exist today, many clients realize that the learning curve is very steep, so they need to start the learning process today so they do not miss out on the significant benefits. Also, C-level executives have realized that they do not have to invest that much to get started (i.e. they don’t have to build their own quantum computer). 

Costs: Compared to classical computing, quantum computing outcomes will be more reliable/accurate, and much less time consuming. All of this has cost-side benefits for our clients. 

Quantum inspired: Finally, we often hear the critique - useful quantum computers are years away. However, and here is what many people are not aware of - many of our clients that are experimenting and learning about quantum algorithms now are using these learnings to improve their classical algorithms and workflows! That means that investing in quantum computing today can have benefits TODAY. 
 
If you are interested in learning more, please reach out to us at Creative Destruction Lab. 

[![Introduction](../figures/youtube.png)](https://youtu.be/hcUpBK2gFis)
