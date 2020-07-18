from utility import *
from openfermion.utils import low_rank_two_body_decomposition
from openfermion.ops import FermionOperator
from openfermion.transforms import jordan_wigner
from tqdm.auto import tqdm  # pip install tqdm


class MeasurementUnitaryGenerator():
    """
    Usage:
        # run the grouping algorithm
        h2o_mcalc = MeasurementGrouper('h2o')
        # get commuting groups
        comm_groups = h2o_mcalc.comm_groups
        # get qwc unitaries
        uqwcs = h2o_mcalc.uqwcs
        # get qwc groups
        qwc_groups = h2o_mcalc.qwc_groups
        # get z unitaries
        uqwcs = h2o_mcalc.uzs
        # get z groups
        z_groups = h2o_mcalc.z_groups
    """

    def __init__(self, mol_sym, basis='sto3g', mapping='jw', do_taper=True, do_fc_partitioning=True,
                 apply_uzs=True, svd_truncation_thresh=-1, verbose=True):
        """
        parameters:
            mol_sym: string representing the molecule type

            basis: orbital basis
            mapping: fermion -> qubit mapping. 'jw' (jordan-wigner) is defualt
            do_taper: whether to do tapering after the mapping
            do_fc_partitioning: whether to partition into fully commuting groups and translate
                to qwc groups. Tradeoff is reducing number of measurement groups vs reducing
                total number of unitaries
            simulate_gates: whether to apply last set of unitaries for transforming
                qwc groups to z-basis. This is not actually needed if all you want
                is the unitaries, and is only for informational purposes. It takes
                a while to run on n2 and nh3
            svd_truncation_thresh: EXPERIMENTAL threshold for singular value truncation in
                if not supplied, don't do svd_truncation
            verbose: whether to print steps
        """

        self.verbose = verbose

        # just a quick check to make sure the molecule is implemented
        valid_mol_syms = ['h2', 'h2o', 'lih', 'n2', 'nh3', 'h4']
        assert mol_sym in valid_mol_syms, \
            f"Provided invalid mol_sym: '{mol_sym}'. Please provide a mol_sym in {valid_mol_syms}"

        # lookup tables
        # choosing the minima from task 1 but not sure this is the right thing to do
        self.lut_geos = {
            'h2': 0.7,
            'h2o': 1,
            'lih': 1.5,
            'n2': 1.2,
            'nh3': 1.1,
            'h4': 95  # not the minimum, chose an angle
        }
        # literally counting the number of electrons from periodic table
        # but not sure this is the right way to do it
        self.lut_n_electrons = {
            'h2': 2,
            'h2o': 10,
            'lih': 4,
            'n2': 14,
            'nh3': 10,
            'h4': 4
        }

        # NOW FOLOW THE STEPS
        self._print(
            "1) Initialise the molecule object in a given basis and with a provided mapping")
        self.mol = get_qubit_hamiltonian(
            mol=mol_sym, geometry=self.lut_geos[mol_sym], basis=basis, qubit_transf=mapping)
        n_orbitals = self._get_num_orbitals(self.mol)
        n_terms = len(self.mol.terms)
        self._print(f"\t{n_orbitals} orbitals")

        if svd_truncation_thresh > 0:
            # TODO - we are repeating a lot of step 1 here. Restructure to avoid this
            self._print("1.5) Applying (experimental) SVD truncation")
            self.mol = self.get_svd_truncated_qubit_hamiltonian(
                mol_sym, basis, mapping, n_orbitals, svd_truncation_thresh)
            self._print(
                f"\t Reduced number of terms from {n_terms} to {len(self.mol.terms)}")

        self._print("2) Optionally apply tapering")
        if do_taper:
            self.mol = taper_hamiltonian(self.mol, n_spin_orbitals=self._get_num_orbitals(self.mol),
                                         n_electrons=self.lut_n_electrons[mol_sym], qubit_transf=mapping)
            n_orbitals = self._get_num_orbitals(self.mol)
            self._print(f"\t{n_orbitals} orbitals")

        if n_orbitals > 8 or not do_fc_partitioning:
            if not do_fc_partitioning:
                self._print(
                    "Skipping FC partitioning and directly getting qwc groups")
            else:
                self._print(
                    "More than 8 orbitals: skipping steps 3), 4) and 5) and directly getting qwc groups")
            qwc_groups = get_qwc_group(self.mol)
            # switch structure for consistency with comm_groups structure
            self.qwc_groups = {i+1: v for i, v in enumerate(qwc_groups)}
            self._print(f"\t{len(self.qwc_groups)} QWC groups,"
                        + f" a {len(self.mol.terms)/ len(self.qwc_groups):.2f} x reduction from {len(self.mol.terms)} terms")
        else:
            self._print("3) Get commuting groups")
            self.comm_groups = get_commuting_group(self.mol)
            self._print(
                f"\t{len(self.comm_groups)} commuting groups,"
                + f" a {len(self.mol.terms)/ len(self.comm_groups):.2f} x reduction from {len(self.mol.terms)} terms")

            self._print(
                "4) For each commuting group get the unitary for transforming to qwc")
            self.uqwcs = {}
            # comm groups is a dict with int keys
            for group_ix in tqdm(self.comm_groups, disable=(not self.verbose)):
                self.uqwcs[group_ix] = get_qwc_unitary(
                    self.comm_groups[group_ix])

            self._print("5) Apply unitaries to get the qwcs")
            self.qwc_groups = {}
            for group_ix in tqdm(self.comm_groups, disable=(not self.verbose)):
                self.qwc_groups[group_ix] = remove_complex(
                    self.uqwcs[group_ix] * self.comm_groups[group_ix] * self.uqwcs[group_ix])

        self._print(
            "6) Get unitaries for rotating everything to the measurable z-basis")
        self.uzs = {}
        for group_ix in tqdm(self.qwc_groups, disable=(not self.verbose)):
            self.uzs[group_ix] = get_zform_unitary(self.qwc_groups[group_ix])

        self.z_groups = {}
        if apply_uzs:
            self._print(
                "7) Finally, apply latter unitaries to move all qwc groups to z-basis")
            for group_ix in tqdm(self.qwc_groups, disable=(not self.verbose)):
                self.z_groups[group_ix] = remove_complex(
                    self.uzs[group_ix] * self.qwc_groups[group_ix] * self.uzs[group_ix])

    def get_svd_truncated_qubit_hamiltonian(self, mol_sym, basis, mapping, n_qubits, thresh):
        """
        This is an experimental attempt at applying the techniques
        from https://arxiv.org/pdf/1907.13117.pdf
        Implementation roughly follows the function `test_rank_reduction`
        from https://github.com/quantumlib/OpenFermion/blob/master/src/openfermion/utils/_low_rank_test.py
        """

        # get molecule object
        g = get_molecular_data(mol_sym, self.lut_geos[mol_sym])
        mol = MolecularData(g, basis, 1, 0)
        mol = run_pyscf(mol)
        # molecule interaction
        ham = mol.get_molecular_hamiltonian()
        # fermion operator
        hamf = get_fermion_operator(ham)
        # decompose with threshold
        (test_eigenvalues, one_body_squares, one_body_correction,
         trunc_error) = low_rank_two_body_decomposition(ham.two_body_tensor,
                                                        truncation_threshold=thresh)

        # Build back operator constant and one-body components.
        trunc_hamf = FermionOperator((), ham.constant)
        one_body_coefficients = (ham.one_body_tensor + one_body_correction)
        for p, q in itertools.product(range(n_qubits), repeat=2):
            term = ((p, 1), (q, 0))
            coefficient = one_body_coefficients[p, q]
            trunc_hamf += FermionOperator(term, coefficient)

        # Build back two-body component.
        for l in range(len(test_eigenvalues)):
            one_body_operator = FermionOperator()
            for p, q in itertools.product(range(n_qubits), repeat=2):
                term = ((p, 1), (q, 0))
                coefficient = one_body_squares[l, p, q]
                one_body_operator += FermionOperator(term, coefficient)
            trunc_hamf += (test_eigenvalues[l] *
                           one_body_operator ** 2)

        if mapping == 'bk':
            trunc_hamq = jordan_wigner(trunc_hamf)
        elif mapping == 'jw':
            trunc_hamq = jordan_wigner(trunc_hamf)
        else:
            raise(ValueError(qubit_transf, 'Unknown mapping specified'))

        return trunc_hamq

    def _print(self, string):
        if self.verbose:
            print(string)

    def _get_num_orbitals(self, mol):
        """
        Hacky way to get number of orbitals for a molecule object
        Probably there is a better way to do it
        """
        max_orbital = 0
        for product_op in mol.terms:
            if product_op:
                mx = max([op[0] for op in product_op])
                if mx > max_orbital:
                    max_orbital = mx
        return max_orbital + 1
