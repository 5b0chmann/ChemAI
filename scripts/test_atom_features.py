from pathlib import Path
from rdkit import Chem
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.ml.atom_features import (get_atom_feature_vector)

smiles = "CC(=O)Nc1ccc(O)cc1" # Paracetamol

mol = Chem.MolFromSmiles(smiles)

for atom in mol.GetAtoms():

    vector = get_atom_feature_vector(atom)

    print(f"Atom {atom.GetIdx()} "
          f"({atom.GetSymbol()}):")

    print(vector)



