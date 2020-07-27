![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 3: Franck-Condon Factors

## Tasks include:
* Calculate the Franck-Condon Factors (and spectra) of molecular Hydrogen using a simple model
* Calculate the Franck-Condon Factors (and spectra) of a more complex molecule (V<sub>3</sub>) using matrix elements
* Calculate the Franck-Condon Factors (and spectra) of that molecule using vibronic sampling. This calculation involves Gaussian Boson Sampling (GBS), which would allow these factors to be calculated using a quantum circuit.

## Task solutions:

Task 1 : Calculating FCF for H2-H2+ molecule

Using the approximation of the harmonic oscillator, we calculate classically the vibronic transitions for given energy levels determining associated Franck Condon Factors. 

<img src="https://github.com/Week3-Group1-CDL2020/CohortProject_2020/blob/master/Project_3_Franck_Condon_Factors/H2_FCF.png" width="800" height="600">



Task 2 : Use matrix elements to calculate FCF and spectra of V<sub>3</sub>

We use FC.cxx and the input file V<sub>3</sub> that contained information about the molecule to generate the following figure
<img src="https://github.com/Week3-Group1-CDL2020/CohortProject_2020/blob/master/Project_3_Franck_Condon_Factors/Task2_plot.png"  width="800" height="400">
We also include the V3_tex.pdf that contains a table of the spectrum assignments. We also placed print statements within the FC.cxx code to learn the Duschinsky Matrix and the displacement vector (for the next task)



Task 3 : Gaussian Boson Sampling (GBS) for calculating FCF and spectra

The data for the input is taken from the last experiment. The sampling seems to converge after 200 samples except for a slight bump at 600 samples. Doing it over 800 samples was taking too long of a time.
<img src="https://github.com/Week3-Group1-CDL2020/CohortProject_2020/blob/master/Project_3_Franck_Condon_Factors/Task3_plot.png" width="800" height="400">

## Business Application
For more details refer to the [Business Application found here](./Business_Application.md)

## Further Challenges:
* An alternative and analogous method to calculating these Franck-Condon Factors using matrix elements is to use a loop hafnian approach. This loop hafnian approach uses GBS which would allow these factors to be calculated using a quantum circuit. Use the result of Task 3 to provide data to a skeleton code provided that uses loop hafnians to calculate the Franck-Condon Factors.
* Explain briefly the similarities and differences between these three methods.
* What are advantages and disadvantages of codes licensed for the public domain and those that are licensed for private use


## Presenting your results in your pull request
For your pull request, consider the following for the presentation of your final results:
- Work entirely in the directory for Project 3.
- Edit this README.md file with a highlight of your main technical results.  Provide links to any other files with your detailed results, e.g. Jupyter notebooks.
- For your Business Application, feel free to provide your answers directly in the 
[Business_Application.md](./Business_Application.md) file.
- Do not directly upload your video file (or any other large files) to the repository.  Instead, provide a link e.g. to a YouTube video, or a Google Drive file.
- Include a file contributions.md that lists the contributions of each group member.
