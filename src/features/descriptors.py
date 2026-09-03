from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski

def calculate_descriptors(smiles):
    """Calculate molecular descriptors for a given SMILES string."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None  # Invalid SMILES string

    return {
        "molecular_weight": Descriptors.MolWt(mol),
        "log_p": Descriptors.MolLogP(mol),
        "h_donors": Lipinski.NumHDonors(mol),
        "h_acceptors": Lipinski.NumHAcceptors(mol),
        "tpsa": Descriptors.TPSA(mol),
        "rotatable_bonds": Lipinski.NumRotatableBonds(mol),
        "ring_count": Lipinski.RingCount(mol),
        "num_atoms": mol.GetNumAtoms(),
        "num_bonds": mol.GetNumBonds(),
    }




  