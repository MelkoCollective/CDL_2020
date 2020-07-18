import tequila as tq
from utility import *
from tqdm.auto import tqdm # pip install tqdm
from MeasurementUnitaryGenerator import MeasurementUnitaryGenerator

#
# Molecules to process
#

class quantumPES:
    def __init__(self):
        self.molecules = [] 
        self.molecules.append("h2".upper())
        self.molecules.append("h2o".upper())
        self.molecules.append("lih".upper())
        self.molecules.append("h4".upper())
        self.molecules.append("n2".upper())
        self.molecules.append("nh3".upper())
        #print(self.molecules)
        
    def haveMol(self,name):

        name = name.upper()
        for m in range(len(self.molecules)):
            if ( self.molecules[m] == name ):
                return True
        return False

    # Experienting zone to abstract parameters for various molecules 
    # We prepare entanglers using  QCC and QWC (from Step 3 and Step 4)

    def prepareMolecule(self,molname,geometry=2.5,basis='sto-3g',n_ents=1,method="BFGS", qubit_transf = 'jw', active_orbitals=None, threshold=1e-6,verbose=True):
            if ( self.haveMol(molname)):

                if ( verbose ): print("Mapping selected: {}".format(qubit_transf))
                # get the measurements - Allows us to access geometries
                
                self.mcalc = MeasurementUnitaryGenerator(molname,mapping = qubit_transf)
                geometry = self.mcalc.lut_geos[molname]
                if ( verbose ): print("Obtained geometry for {} is {}".format(molname, geometry))

                if ( verbose ): print("\n\nCalculating QCC for ", molname.upper())
                if ( verbose ): print("Basis: {}\nGeometry: {}\nEntanglers: {}\nActive Orbitals: {}".format(basis,geometry,n_ents,active_orbitals))
                
                # 
                
                xyz_data = get_molecular_data(molname, geometry=geometry, xyz_format=True)
                mol = tq.quantumchemistry.Molecule(geometry=xyz_data, basis_set=basis, active_orbitals = active_orbitals)
                hf_reference = hf_occ(2*mol.n_orbitals, mol.n_electrons)
                
                # FCI energy calculation
                
                E_FCI = mol.compute_energy(method='fci')
                
                # Hamiltonian
                
                H = mol.make_hamiltonian()

                if ( verbose ): print("\nHamiltonian has {} terms\n".format(len(H)))

                #Define number of entanglers to enter ansatz
                #Rank entanglers using energy gradient criterion
                ranked_entangler_groupings = generate_QCC_gradient_groupings(H.to_openfermion(), 
                                                                             2*mol.n_orbitals, 
                                                                             hf_reference, 
                                                                             cutoff=threshold)

                #print('Grouping gradient magnitudes (Grouping : Gradient magnitude):')
                #for i in range(len(ranked_entangler_groupings)):
                #    print('{} : {}'.format(i+1,ranked_entangler_groupings[i][1]))


                entanglers = get_QCC_entanglers(ranked_entangler_groupings, n_ents, 2*mol.n_orbitals)

                #print('\nSelected entanglers:')
                #for ent in entanglers:
                #    print(ent)

                #Mean-field part of U (Omega):    
                U_MF = construct_QMF_ansatz(n_qubits = 2*mol.n_orbitals)
                #Entangling part of U:
                U_ENT = construct_QCC_ansatz(entanglers)
                U_QCC = U_MF + U_ENT                    

                E = tq.ExpectationValue(H=H, U=U_QCC)
                
                if ( verbose ): print("Full QCC Circuit from Step 3: \n", U_QCC)

                initial_vals = init_qcc_params(hf_reference, E.extract_variables())
                if ( verbose ): print("Initial Values: {}".format(initial_vals))

                #Minimize wrt the entangler amplitude and MF angles:
                result = tq.minimize(objective=E, method=method, initial_values=initial_vals, tol=1.e-6)

                if ( verbose ): print('\nObtained QCC energy for {} ({} entanglers): {}'.format(molname.upper(),len(entanglers), result.energy))
                if ( verbose ): print('Compare to FCI energy: {}\n'.format(E_FCI))
                
                # TODO: ================= Construct entanglers from mcalc (task 4) ========================================
                
                #print('First commuting group')
                #print(mcalc.comm_groups[1])
                #print('\n')
                #print('First QWC group')
                #print(mcalc.qwc_groups[1])
                #print('\n')
                #print('First Z group')
                #print(mcalc.z_groups[1])
                #print('\n')
                
                # Possibly on ly need these
                #print('First qwc unitary')
                #print(mcalc.uqwcs[1])
                #print('\n')
                #print('First z unitary')
                #print(mcalc.uzs[1])



                
                # 
                # Perform the similar operation as U_MF + U_ENT using the mcalc entanglers
                #
                # We then need to make a choice: Do we compare both methods, two circuits? Or pick one method?
                
                mcalc_entanglers = []
                
                if hasattr(self.mcalc, 'uqwcs'):
                    mcalc_entanglers.append(self.mcalc.uqwcs[1])
                    
                if hasattr(self.mcalc, 'uzs'):
                    mcalc_entanglers.append(self.mcalc.uzs[1])
                    
                if ( verbose ): print("\nMCalc Entanglers: \n", mcalc_entanglers)
                
                # Memorize the last compute
                
                self.comp_n_ents = n_ents
                self.comp_basis = basis
                self.comp_mol = molname
                self.comp_E_QCC = result.energy
                self.comp_U_QCC = U_QCC                   # Entanglers from team step 3.
                #self.comp_entanglers = entanglers        # Entanglers from my version of Step 3. Replace with U_QCC
                self.comp_E_FCI = E_FCI
                self.comp_initial_vals = initial_vals
                self.comp_qubit_transf = qubit_transf
                
            else:
                print("molecule not known")

    # Prepare the list of circuits that we want to process
    def prepareCircuits(self):
        
        H = tq.QubitHamiltonian.from_openfermion(get_qubit_hamiltonian(self.comp_mol, 2, self.comp_basis, qubit_transf=self.comp_qubit_transf)) 
        
        # Create an empty list of circuits
        
        Circuits = []
        
        # Create as many circuits as we need: U_QCC + Entangler
        
        
        print("\n=======================================\n", self.comp_U_QCC, "\n=======================================\n")
        
        if hasattr(self.mcalc, 'uqwcs'):
            for gate in self.mcalc.uqwcs[1]:
                if (self.formatEntangler(gate)): 
                    print("uqwcs..................................")
                    a = tq.Variable("tau_0") # Why do we pick tau ??? This is for H2. What about others?
                    print(self.formatEntangler(gate))
                    Circuits.append(self.comp_U_QCC + tq.gates.ExpPauli(paulistring=tq.PauliString.from_string(self.formatEntangler(gate)), angle=a))
        if hasattr(self.mcalc, 'uzs'):
            for gate in self.mcalc.uzs[1]:
                if (self.formatEntangler(gate)): 
                    print("uzs..................................")
                    a = tq.Variable("tau_0") # Why do we pick tau ??? This is for H2. What about others?
                    print(self.formatEntangler(gate))
                    Circuits.append(self.comp_U_QCC + tq.gates.ExpPauli(paulistring=tq.PauliString.from_string(self.formatEntangler(gate)), angle=a))

        print("{} Circuits generated".format(len(Circuits)))

        self.comp_Circuits = Circuits
         
        return (Circuits)
    
        
    def runCircuits(self, useIBM = False, backend="qiskit", device='ibmq_qasm_simulator' ):
        
        print("Constructing circuit(s) for {}".format(self.comp_mol.upper()))
        H = tq.QubitHamiltonian.from_openfermion(get_qubit_hamiltonian(self.comp_mol, 2, self.comp_basis, qubit_transf=self.comp_qubit_transf)) 
                
        print("============= {} Circuits to execute =============".format(len(self.comp_Circuits)))
        
        c_i = 0
        for circuit in self.comp_Circuits:
            print("Circuit #", c_i)
            c_i = c_i + 1
              
            circ = tq.circuit.compiler.compile_exponential_pauli_gate(circuit)
            tq.draw(circ, backend="qiskit")

            E = tq.ExpectationValue(H=H, U=circuit)
            vars =self.comp_initial_vals
            E_sim = tq.simulate(E, variables=vars)
            
            if ( useIBM ):
                # list of devices available can be found in ibmq account page
                max_try = 3
                while (max_try>0):
                    try:
                        E_qc = tq.simulate(E, variables=vars, samples=100, backend=backend, device=device)

                        print("Calculated E_sim, E_qc as : ", E_sim, E_qc )
                        max_try = 0
                        #print("Calculated vars here      : ", vars)
                    except:
                        print("Error communicating with backend.")
                        max_try = max_try - 1
                        pass
            else:
                print("Calculated E_sim as : ", E_sim )
                    
    # For each selected entanglers we will need to compute a separate circuit
    # We we need to create an array of gates
    # we will need to transform the result from Step 3 into a result that can be used here
    #  [X0 Y1 X2 X3] ==> X(0)Y(1)X(2)X(3)

    def formatEntangler(self,e):
        toString = ""
        for t in e.terms:
            for c,axis in t:
                toString += axis + "(" + str(c) + ")"
        return(toString)
            
            