![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

A brief example for each question is included for the 
[Traveling Salesman Problem.](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

## Step 1: Explain the technical problem you solved in this exercise

The technical problem is to train an RBM (Restricted Boltzmann Machine) to learn information about the H2 molecule and Rydberg atoms, specifically how the potential energy stored in the H2 molecule varies as the distance between the H atoms changes.

There is a chemical bond between the two atoms and there is a force of attraction and replusion between these two atoms. The balance between these two forces determines the distance that separates the atoms in a chemical bond (called the bond length).

The potential energy stored in the molecule can be plotted as a function of the two atoms' separation r. The attractive and repulsive forces will be in equilibrium at the very minimum point on the curves.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

A few types of real world problems this solution can solve involves drug development, materials research and study of the natural processes that can lead to improvements in fertilizer and chemical manufacturing.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

A few potential customers for this solution include :

1) Optima Chemical https://optimachem.com/development-services/
2) GVK Bio https://www.gvkbio.com/chemical-development-services/
3) Anuvia Plant Nutrients https://www.anuviaplantnutrients.com/

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language


--------------
## Step 1: Explain the technical problem you solved in this exercise
There is a reason cartoons depict chemists as mad scientist who accidentally blow up their labs: predicting how chemicals will react when combined is often difficult. To make a prediction, we must understand how molecules behave as they collide with other molecules. This is determined by the chemical bond between the atoms of the molecule, which depends on the forces of attraction between the electrons and protons that make up the molecule. The balance between these forces determines the distance that separates the atoms in a chemical bond (called the bond length). Because electrons and protons are governed by the laws of quantum mechanics, these calculations are difficult and require colossal computing efforts.

We have speeded up this calculation and made it massively cheaper by training a machine-learning algorithm called a Restricted Boltzmann Machine (RBM) to learn information about the H2 molecule. Specifically, it learns how the potential energy stored in the H2 molecule varies as the distance between the H atoms changes. Now, instead of making the full quantum mechanical calculation to find the forces inside the molecule, you can just ask the RBM for what the energies will be for the parameters you are interested in. The RBM will make accurate predictions even for parameter values it has not seen before and much cheaper and faster than the full calculation. 

We have also started work on training the RBM for other types of molecules, such as LiH and BeH2, which will soon enable us to make predictions about chemical reactions and material properties.


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Once the RBM has been trained on more molecules than H2, it can be used as a piece in computational chemistry software. Instead of making various approximations justified by chemists to do the calculation fast, you can find the forces from the RBM that has been trained on the real quantum data and gives accurate predictions. Now you can use the forces to predict for example at what temperature a chemical reaction can occur, or how fast a reaction happens. 

These calculations have very wide applicability on the chemical industry. A large fraction of their R&D has to do with producin new chemicals, or increasing the efficiency of current processes. Examples are drug development, and fertilizer and chemical manufacturing. In drug development it is important to be able to test as many chemicals in simulation as possible to find out oif it can react in the right way. In fertilizer and chemical manufacturing its is important to find the most efficient ways of creating the product, so accurancy matters a great deal. 

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Potential customers that would want to use our RBM to solve their problems in chemistry include:

1) Optima Chemical https://optimachem.com/development-services/
2) GVK Bio https://www.gvkbio.com/chemical-development-services/
3) Anuvia Plant Nutrients https://www.anuviaplantnutrients.com/

[Why these, can we have some explanation?]

Furthermore, computational chemistry software providers, such as Schrödinger (https://www.schrodinger.com/) could be interested in licensing the technology to include it in their software. Their business depends on providing state-of-the-art computational chemistry tools that perform calculations fast and accurately. Our technology, once it is fully trained, would provide a valuable speedup for some of their customers. 
