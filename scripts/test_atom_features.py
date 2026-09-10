from pathlib import Path
from rdkit import Chem
import pandas as pd
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.ml.atom_features import (get_atom_feature_vector)

smiles = "CC(=O)Nc1ccc(O)cc1" # Paracetamol

mol = Chem.MolFromSmiles(smiles)

feature_matrix = []

for atom in mol.GetAtoms():

    vector = get_atom_feature_vector(atom)

    feature_matrix.append(vector)

columns = [
    "atomic_number",
    "degree",
    "formal_charge",
    "valence",
    "hybridization",
    "is_aromatic",
    "is_in_ring",
    "ring_size",
    "num_hydrogens",
    "neighbor_c",
    "neighbor_n",
    "neighbor_o",
    "neighbor_halogen",
    "single_bonds",
    "double_bonds",
    "triple_bonds"
]

df = pd.DataFrame(feature_matrix, columns=columns)

print(df)



