from rdkit import Chem
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.spectroscopy.functional_groups import FUNCTIONAL_GROUPS

smiles = "NCC1(CC(=O)O)CCCCC1"  # Gabapentin

mol = Chem.MolFromSmiles(smiles)

pattern = Chem.MolFromSmarts(FUNCTIONAL_GROUPS["Ketone"])

print(mol.HasSubstructMatch(pattern))
print(mol.GetSubstructMatches(pattern))

print("Gabapentin:", mol.HasSubstructMatch(pattern))