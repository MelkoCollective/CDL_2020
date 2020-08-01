import csv 
import numpy as np
from tabu import TabuSampler
from collections import defaultdict
from dimod import BinaryQuadraticModel
from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridSampler
import neal

class GroundStateEnergy:

    def data(self):
        return self.coeff

    # Initialize with coefficient data
    def __init__(self,file):

        self.coeffs = {} # New dictionary method
        self.coeff = []  # Original method
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            first = True
            previous_R = 0.0  # The data set has a misalignment for the exact energy values for each R
                              # We fix this error at loading time by storing the correct value in the previous row
            for row in reader:
                if ( first ): 
                    first = False
                    continue

                row = list(map(float, row)) 
                self.coeff.append(row)
                
                # New method starts here
                
                R = row[0]
                    
                # Additional data storage for Week 4

                self.coeffs[R] = ( {'g0': row[1], 'g1':row[2], 'g2':row[3], 'g3':row[4], 'g4':row[5], 'e':row[6], 'g3add':0.0},
                                   {'c_a' : 0.0, 'c_b' : 0.0, 'c_c':0.0, 'a1':0.0, 'a2':0.0, 'a3':0.0 })
                
                # Fix the data set anomaly
                if ( previous_R > 0 ):
                    self.coeffs[previous_R][0]['e'] = self.coeffs[R][0]['e']
                
                # Calculate the q_coeffs from the g_values
                # WARNING: The value of g3 will be changed by this. Only call calculate_coeffs ONCE at load time
                #          Do not use calculate_coeffs anywhere else.
                
                (c_a,c_b,c_c,a1,a2,a3) = self.calculate_coeffs(R,self.coeffs[R][0])
                
                self.coeffs[R][1]['a1'] = a1
                self.coeffs[R][1]['a2'] = a2
                self.coeffs[R][1]['a3'] = a3
                self.coeffs[R][1]['c_a'] = c_a
                self.coeffs[R][1]['c_b'] = c_b
                self.coeffs[R][1]['c_c'] = c_c
                #self.coeffs[R][1]['g3add'] = g3add
                
                #print("Returned QUBO values: ", self.get_qubo_coeffs(R))
                
                previous_R = R
                
                
                
        self.useQPU = False
        self.useHyb = False
        self.useNeal = False
        self.useTabu = True
        
        #print(self.data)
        #print(self.coeffs[3.1][0])
        #print(self.coeffs[3.1][1])

        print(self.get_available_R())
        
        #for r in self.get_available_qubo_R():
        #    print("--------------------- radius ", r, " ------------------" )
        #    print(self.get_g_values(r))
        #    print(self.get_qubo_coeffs(r))
        
    # Return the available R values for the qubo
    def get_available_R(self):
        return list(self.coeffs.keys())
    
    # Return the qubo coeffs plus the g3_addition 
    def get_qubo_coeffs(self,R):
        return(self.coeffs[R][1])

    def get_g_values(self,R):
        return(self.coeffs[R][0])
    
    # Given 2 binary spins state for a given R (which can be obtained by a ising solver of your choice),
    # calculate the ground state energy
    def get_energy_from_binary_spins(self,R,x0,x1):
        
        g_values = self.get_g_values(R)
        g3_addition = g_values['g3add']
        g0 = g_values['g0']
        g1 = g_values['g1']
        g2 = g_values['g2']
        g3 = g_values['g3']

        q_coeff = self.get_qubo_coeffs(R)
        a1 = q_coeff['a1']
        a2 = q_coeff['a2']
        a3 = q_coeff['a3']
        
        Y = 4 * x0 * x1 + (2*a2 - 2*a3) * x0 + (2*a2-2*a3) * x1 + a3 - 2*a2 + a1

        # convert x0,x1 to ising spins 
        
        sz0 = ( 2 * x0 ) -1 
        sz1 = ( 2 * x1 ) -1 

        # Get hx1 and hx2 in :
        # hx**2 + 2*g3*hx = Y
        # a = 1, b = 2g3, c = -Y
        
        a = 1
        b = 2 * g3
        c = -Y

        #print("a,b,c,b**2-4*a*c : ", a,b,c,b**2-4*a*c)
        
        # Solve H1 for x (minimum of the two possibilities)
        hx1 = ( -b + np.sqrt(b**2-4*a*c)) / (2 * a ) 
        hx2 = ( -b - np.sqrt(b**2-4*a*c)) / (2 * a ) 

        if ( hx2 < hx1):
            swp = hx2
            hx2 = hx1
            hx1 = swp

        # Add g3_addition to hx1
        hx1 += g3_addition
        H0_ver = (g1 * sz0) + (g2 * sz1) + (g3 * sz0 * sz1) 
        H0 = hx1
        H = H0 + g0

        return (H)

        
        
    # Given 2 spins state for a given R (which can be obtained by a ising solver of your choice),
    # calculate the ground state energy
    def get_energy_from_ising_spins(self,R,sz0,sz1):

        g_values = self.get_g_values(R)
        g3_addition = g_values['g3add']
        g0 = g_values['g0']
        g1 = g_values['g1']
        g2 = g_values['g2']
        g3 = g_values['g3']

        q_coeff = self.get_qubo_coeffs(R)
        a1 = q_coeff['a1']
        a2 = q_coeff['a2']
        a3 = q_coeff['a3']
        
        # Step 4: Calculate Y = ( a1 + a2( sz0 + sz1 ) + a3 (sz0*sz1))
        Y = ( a1 + a2 * ( sz0 + sz1 ) + a3 * (sz0 * sz1))

        # Convert to get x0,x1
        #x0 = (sz0 + 1) / 2
        #x1 = (sz1 + 1) / 2

        # Get hx1 and hx2 in :
        # hx**2 + 2*g3*hx = Y
        # a = 1, b = 2g3, c = -Y

        a = 1
        b = 2 * g3
        c = -Y

        #print("a,b,c,b**2-4*a*c : ", a,b,c,b**2-4*a*c)
        
        # Solve H1 for x (minimum of the two possibilities)
        hx1 = ( -b + np.sqrt(b**2-4*a*c)) / (2 * a ) 
        hx2 = ( -b - np.sqrt(b**2-4*a*c)) / (2 * a ) 

        if ( hx2 < hx1):
            swp = hx2
            hx2 = hx1
            hx1 = swp

        # Add g3_addition to hx1
        hx1 += g3_addition
        H0_ver = (g1 * sz0) + (g2 * sz1) + (g3 * sz0 * sz1) 
        H0 = hx1
        H = H0 + g0
        
        return(H)


    def solve_ising(self,R,samples,exact,verbose,useQPU=False,useHyb=False,useNeal=False,useTabu=False):
        return self.solve(R,False,samples,exact,verbose,useQPU,useHyb,useNeal,useTabu)

    def solve_qubo(self,R,samples,exact,verbose,useQPU=False,useHyb=False,useNeal=False,useTabu=False):
        return self.solve(R,True,samples,exact,verbose,useQPU,useHyb,useNeal,useTabu)

    # Calculate the QUBO coefficents from the g_values
    # Use this function when loading the data. Some variables will get modified.
    # Do not run more than once for a given R
    def calculate_coeffs(self,R,g_values):

        g1 = g_values['g1']
        g2 = g_values['g2']
        g3 = g_values['g3']
        g4 = g_values['g4']
        
        # Step 1: If |g1| + |g2| + |g4| >= |g3| : g3 += |g1| + |g2| + |g4|
        # Remember the g3 addition for later
        g3_addition = 0
        if ( abs(g1) + abs(g2) + abs(g4) >= abs(g3)) :
            g3_addition = (abs(g1)+abs(g2)+abs(g4))
            g3 = (abs(g3) + g3_addition)

        # Step 1b: calculate a1, a2, a3
        a1 = g1**2 + g2**2 + g3**2 + 2 * g4**2
        a2 = 2 * ( g1 + g2) * g3
        a3 = 2 * (g1*g2 - g4**2 + g3**2)

        # Step 2 : Solve H0**2 + 2g3H0 = a1 + a2( sz0 + sz1 ) + a3 (sz0*sz1) = Y
        # (the squared H0 hamiltonian)
        # where sz0 is sigma z bit 0, ...
        # Convert szi -> (2 xi - 1) (ising  to qubo conversion)
        # then simplify the equation to obtain the quadratic coeeficients of a two qubit system
        # Calculated Q matrix:
        #   |  (2a2-2a3)    2a3     |
        #   |     2a3    (2a2-2a3)  |

        c_a = 2 * a2 - 2 * a3
        c_b = 4 * a3
        
        qubo_values = (c_a,c_b,0.0,a1,a2,a3)
        
        g_values['g3'] = g3  # Save the new value of g3. Requires g3_addition
        g_values['g3add'] = g3_addition 
        
        #print("g3_addition is : ", g3_addition)
        #print("QUBO Values are: ", qubo_values)
        
        return (qubo_values)
    
    
    # Solve the energy for the given radius and coefficients
    def solve(self,R,qubo,samples,exact,verbose,useQPU,useHyb,useNeal,useTabu):

        use_QUBO = qubo

        # We obtain the calculations performed at load time
        c_coeffs = self.get_qubo_coeffs(R)
        
        c_a = c_coeffs['c_a']
        c_b = c_coeffs['c_b']
        c_c = c_coeffs['c_c']
        a1 = c_coeffs['a1']
        a2 = c_coeffs['a2']
        a3 = c_coeffs['a3']
        
        g_values = self.get_g_values(R)
        g0 = g_values['g0']
        g1 = g_values['g1']
        g2 = g_values['g2']
        g3 = g_values['g3']
        g4 = g_values['g4']
        e = g_values['e']
        g3_addition = g_values['g3add']
        
        # Solve the equation. First solution is lowest energy
        if use_QUBO:

            #Using QUBO
            Q=defaultdict(float)
            Q[0,0] = c_a
            Q[0,1] = c_b
            Q[1,0] = c_b
            Q[1,1] = c_a 

            #Q = [(2 * a2 - 2 * a3, 2 * a3),(2 * a3,2 * a2 - 2 * a3 )]
            offset = 0
            
            
            if ( useQPU ):
                chain_strength = 4
                if (verbose==True): print("Solving using the DWaveSampler on the QPU...")
                sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
                sampleset = sampler.sample_qubo(Q, num_reads=samples,chain_strength = chain_strength)
            elif ( useHyb ): 
                if (verbose==True): print("Solving using the LeapHybridSolver...")
                time_limit = 3
                bqm = BinaryQuadraticModel.from_qubo(Q, offset=offset)
                sampler = LeapHybridSampler()
                sampleset = sampler.sample(bqm, time_limit = time_limit)
            elif ( useNeal ): 
                if (verbose==True): print("Solving using the Leap SimulatedAnnealing...")
                bqm = BinaryQuadraticModel.from_qubo(Q, offset=offset)
                sampler = neal.SimulatedAnnealingSampler()
                sampleset = sampler.sample(bqm, num_reads = samples)
            else:
                if (verbose==True): print("Solving using the TabuSampler...")
                sampler = TabuSampler()
                bqm = BinaryQuadraticModel.from_qubo(Q, offset=offset)
                sampleset = sampler.sample(bqm, num_reads = samples)

            if ( verbose==True ): print(sampleset.first.sample)
            if (verbose==True): print(sampleset)

            # Step 3: Get x0 and x1 for first energy result
            for set in sampleset.data():
                x0 = set.sample[0]
                x1 = set.sample[1]
                energy = set.energy
                if (verbose==True): print("x0,x1,ener : ",x0,x1,energy)
                break

            H_b = self.get_energy_from_binary_spins(R,x0,x1)
            
            Y = 4 * x0 * x1 + (2*a2 - 2*a3) * x0 + (2*a2-2*a3) * x1 + a3 - 2*a2 + a1

            # convert x0,x1 to ising spins 
            sz0 = ( 2 * x0 ) -1 
            sz1 = ( 2 * x1 ) -1 

        else:

            # Using SPIN (ising): H = h_1 * s_1 + h_2 * s_2 + J_{1,2} * s_1 *s_2
            sampler = TabuSampler()
            response = sampler.sample_ising({'a': c_a, 'b': c_a}, {('a', 'b'): c_b}, num_reads = samples)

            if (verbose==True): print(response)

            for set in response.data():
                sz0 = set.sample['a']
                sz1 = set.sample['b']
                energy = set.energy
                if (verbose==True): print("sz0,sz1,ener : ",sz0,sz1,energy)
                break

            H_b = self.get_energy_from_ising_spins(R,sz0,sz1)
            
            # Step 4: Calculate Y = ( a1 + a2( sz0 + sz1 ) + a3 (sz0*sz1))
            Y = ( a1 + a2 * ( sz0 + sz1 ) + a3 * (sz0 * sz1))

            # Convert to get x0,x1
            x0 = (sz0 + 1) / 2
            x1 = (sz1 + 1) / 2


        # Get hx1 and hx2 in :
        # hx**2 + 2*g3*hx = Y
        # a = 1, b = 2g3, c = -Y
        a = 1
        b = 2 * g3
        c = -Y

        #print("a,b,c,b**2-4*a*c : ", a,b,c,b**2-4*a*c)
        
        # Solve H1 for x (minimum of the two possibilities)
        hx1 = ( -b + np.sqrt(b**2-4*a*c)) / (2 * a ) 
        hx2 = ( -b - np.sqrt(b**2-4*a*c)) / (2 * a ) 

        if ( hx2 < hx1):
            swp = hx2
            hx2 = hx1
            hx1 = swp

        # Add g3_addition to hx1
        hx1 += g3_addition
        H0_ver = (g1 * sz0) + (g2 * sz1) + (g3 * sz0 * sz1) 
        H0 = hx1
        H = H0 + g0

        assert( H_b == H )
        
        return (H)

