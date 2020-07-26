![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 3: Franck-Condon Factors

This project will guide you through calculating Franck-Condon Factors, which is related to the intensities in spectra of vibrational transitions across electronic surfaces. Spectra can be measured through experiments, but having accurate theoretical calculations of these Franck-Condon Factors allow scientists to instead predict these experimental results. This is especially useful if the chemical species is expensive, difficult to acquire or difficult to study or if the experiment itself is expensive or difficult.

A very brief introduction to the main ideas behind the project are
[here.](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/CDL_2020_docs.pdf)

In our [Project3_LandingPage.pdf](https://github.com/CDL-Quantum/CohortProject_2020/blob/master/Project_3_Franck_Condon_Factors/Project3_LandingPage.pdf), we provide more technical information about the chemistry and physics behind these Franck-Condon Factors and we encourage you to explore more literature if interested.  Click on this link to begin learning about your tasks for this week!

## Tasks include:
* Calculate the Franck-Condon Factors (and spectra) of molecular Hydrogen using a simple model
* Calculate the Franck-Condon Factors (and spectra) of a more complex molecule (V<sub>3</sub>) using matrix elements
* Calculate the Franck-Condon Factors (and spectra) of that molecule using vibronic sampling. This calculation involves Gaussian Boson Sampling (GBS), which would allow these factors to be calculated using a quantum circuit.


#### Task 1: Solution 
In this task, we calculated the Frank-Condon factors for H2-H2+ molecules using the harmonic oscillator approximation. The jupyter notebook with solutions is here: [Task1.ipynb](Task1.ipynb)


![Task1](task1_fig1.png)


#### Task2: Solution
In task two, we compiled the FC.cxx code. The program was able to generate the Frank-Codon factors for the H2-H2+ molecule. The figure of the spectra is below

![Task2](task2_fig1.png)


#### Task3: Solution
In task three, we simulated Gaussian Boson sampling to compute the Frank-Codon factors. This required us to modify the code from task 2 to generate the required input file. After
we had the correct input file our code was able to generate a spectra which matched what was generated for task 2.

The modifified task2 code is here: [modified task2 code](Task2Code/FCC.cxx)

The jupyter notebook for our solution is here: [jupyter notebook for task3](Task3.ipynb)

We did a sweep over a number of samples starting from 10 up to 10000. We found that convergence happens somewhere around 333~1000 samples.

The ouput of our jupyter notebook is below.

![Task3](task3_fig1.png)


## Further Challenges:
* An alternative and analogous method to calculating these Franck-Condon Factors using matrix elements is to use a loop hafnian approach. This loop hafnian approach uses GBS which would allow these factors to be calculated using a quantum circuit. Use the result of Task 3 to provide data to a skeleton code provided that uses loop hafnians to calculate the Franck-Condon Factors.
* Explain briefly the similarities and differences between these three methods.
* What are advantages and disadvantages of codes licensed for the public domain and those that are licensed for private use

## Business Application

The questions presented in Project 3 landing page have been addressed extensively [here](https://github.com/CDL2020Week3Cohort6/CohortProject_2020/blob/master/Project_3_Franck_Condon_Factors/Business_Applications_Q&A.md).


For more details about Business Applications refer to the [Business Application found here](./Business_Application.md).

