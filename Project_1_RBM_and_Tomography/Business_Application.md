![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum-assisted Machine Learning of Material Properties

## Step 1: Explain the technical problem you solved in this exercise
There is a reason cartoons depict chemists as mad scientist who accidentally blow up their labs: predicting how chemicals will react when combined is often difficult. To make a prediction, we must understand how molecules behave as they collide with other molecules. This is determined by the chemical bond between the atoms of the molecule, which depends on the forces of attraction between the electrons and protons that make up the molecule. The balance between these forces determines the distance that separates the atoms in a chemical bond (called the bond length). Because electrons and protons are governed by the laws of quantum mechanics, these calculations are difficult and require colossal computing efforts.

We have speeded up this calculation and made it massively cheaper by training a machine-learning algorithm called a Restricted Boltzmann Machine (RBM) to learn information about the H2 molecule. Specifically, it learns how the potential energy stored in the H2 molecule varies as the distance between the H atoms changes. Now, instead of making the full quantum mechanical calculation to find the forces inside the molecule, you can just ask the RBM for what the energies will be for the parameters you are interested in. The RBM will make accurate predictions even for parameter values it has not seen before and much cheaper and faster than the full calculation. As a first example we have calculated in WHICH NOTEBOOK material properties of a hydrogen gas.

We have also started work on training the RBM for other types of molecules, such as LiH and BeH2, which will soon enable us to make predictions about chemical reactions and material properties.


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Once the RBM has been trained on more molecules than H2, it can be used as a piece in computational chemistry software. Instead of making various approximations justified by chemists to do the calculation fast, you can find the forces from the RBM that has been trained on the real quantum data and gives accurate predictions. Now you can use the forces to predict for example at what temperature a chemical reaction can occur, or how fast a reaction happens. 

These calculations have very wide applicability on the chemical industry. A large fraction of their R&D has to do with producing new chemicals, or increasing the efficiency of current processes. Examples are drug development, and fertilizer and chemical manufacturing. In drug development it is important to be able to test as many chemicals in simulation as possible to find out if it can react in the right way. In fertilizer and chemical manufacturing it is important to find the most efficient way of creating the product, so accurancy matters a great deal. 

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Potential customers that would want to use our RBM to solve their problems in chemistry include:

1) Optima Chemical https://optimachem.com/development-services/

Optima Chemicals helps companies and startups with a series of complex chemical experiments and being able to make accurate predictions about molecular energies faster will help in their development process.

2) GVK Bio https://www.gvkbio.com/chemical-development-services/

GVK BIO offers a spectrum of chemical development services. Equipped with advanced process and analytical instrumentation, GVK BIO’s team of scientists supports all kinds of chemical development needs, offering integrated, continuous service through the drug development life cycle. Having this algorithm to predict variations in molecular energies appears to fit in right with their needs.

3) Anuvia Plant Nutrients https://www.anuviaplantnutrients.com/

Anuvia's novel, bio-based product accelerates natural principals to deliver the nutrition plants need for immediate and long-term health. Calculating molecular energies is a key part of fertilizer and other plant related chemical product development and this algorithm assits in doing that faster and more accurately.

Furthermore, computational chemistry software providers, such as Schrödinger (https://www.schrodinger.com/) could be interested in licensing the technology to include it in their software. Their business depends on providing state-of-the-art computational chemistry tools that perform calculations fast and accurately. Our technology, once it is fully trained, would provide a valuable speedup for some of their customers. 

  4) Link to Video : https://drive.google.com/file/d/1YMf2RjHjwtpx15PBb_7TX2ZB5h9nrN8L/view?usp=sharing
