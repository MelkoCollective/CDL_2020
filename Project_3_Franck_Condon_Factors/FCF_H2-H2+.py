from math import factorial
from numpy import sqrt, pi, exp, zeros
from numpy.polynomial.hermite import hermval
from numpy.polynomial.legendre import leggauss

#################################                                                                                
########## CONSTANTS ############                                                                                
#################################                                                                                
hbar=1.0
amu_to_me=1822.888486209
invcm_to_invEh=100.0*5.29177210903*pow(10.,-11.)*137.036
AngtoBohr=1.88973

################################                                                                                 
######## INPUT PARAMETERS ######                                                                                 
######## CAN BE MODIFIED  ######                                                                                 
################################                                                                                 

# Define integration bounds for FCFs                                                                             
quadraturepoints=5000
R_min=-5.0  #Ang                                                                                                 
R_max=5.0   #Ang                                                                                                 

# Number of ground/excited state modes to calculate FCFs for                                                     
n_0=3
n_p=3

# Information about the diatomic system                                                                          
mass_of_diatomic=2.01588  #amu                                                                                   
omega_0=4401.0            #cm-1                                                                                  
omega_p=2322.0            #cm-1                                                                                  
eqgeom_0=0.742            #Ang                                                                                   
eqgeom_p=1.057            #Ang                                                                                   

#################################     
######## INITIAL SETUP ##########                                                                                
#################################                                                                                

# CONVERT TO ATOMIC UNITS                                                                                        
mass_of_diatomic*=amu_to_me
omega_0*=invcm_to_invEh
omega_p*=invcm_to_invEh


eqgeom_0*=AngtoBohr
eqgeom_p*=AngtoBohr
R_min*=AngtoBohr
R_max*=AngtoBohr


# CALCULATE ALPHA PARAMETER                                                                                      
alpha_0=mass_of_diatomic*omega_0/hbar
alpha_p=mass_of_diatomic*omega_p/hbar


#####################################                                                                            
## CALCULATE HARMONIC WAVEFUNCTION ##                                                                            
#####################################                                                                            

def psi (alpha,eqgeom,R,state):
    n=state
    prefactor=pow(alpha/pi,0.25)/(sqrt(pow(2.0,n)*factorial(n)))
    coeffs=zeros(n+1,float)
    coeffs[n]=1.0
    hermpoly=hermval(sqrt(alpha)*(R-eqgeom),coeffs)
        return prefactor*exp(-0.5*alpha*(R-eqgeom)**2)*hermpoly


#####################################                                                                            
### USE GAUSS-LEGENDRE QUADRATURE ###                                                                            
###       TO PERFORM INTEGRAL     ###                                                                            
#####################################                                                                            

GLquad=leggauss(quadraturepoints)
print("n_0    n_p      FC")
for i in range(n_0):
    E_0=hbar*omega_0*(i+0.5)/invcm_to_invEh
    for j in range(n_p):
        E_p=hbar*omega_p*(j+0.5)/invcm_to_invEh
        overlap=0.0
        for p in range(quadraturepoints):

            #Coordinate Transformation to expand bounds of integration                                           
            newpoint=0.5*(R_max-R_min)*GLquad[0][p]+0.5*(R_max+R_min)
            newweight=0.5*(R_max-R_min)*GLquad[1][p]

            #Perform numerical integration to calculate FC Factor                                                
            overlap+= psi(alpha_0,eqgeom_0, newpoint,i)*psi(alpha_p,eqgeom_p,newpoint,j)*newweight

        #####################################                                                                    
        ########## PRINT FC FACTORS #########                                                                    
	#####################################                                                                    
        FC=overlap*overlap
        if (i==0 and j==0):
            reference=FC
        if (FC>pow(10.,-3)):
            print(f'{i:3} {j:5} {FC/reference:10.3f}')
