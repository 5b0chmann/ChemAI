from pathlib import Path
from rdkit import Chem
from rdkit.Chem import AllChem
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.ml.electronic_features import(get_gasteiger_charge,
                                       get_mean_neighbor_charge,
                                       get_max_neighbor_charge,
                                       get_min_neighbor_charge)

smiles = "CC(=O)Nc1ccc(O)cc1"  # Paracetamol

mol = Chem.MolFromSmiles(smiles)

AllChem.ComputeGasteigerCharges(mol)

print("\nParacetamol")
print("-" * 60)

for atom in mol.GetAtoms():

    print(f"Atom {atom.GetIdx():2d} "
          f"{atom.GetSymbol():2s} "
          f"Charge= {get_gasteiger_charge(atom): .4f} ",
          f"MeanNbr={get_mean_neighbor_charge(atom): .4f}")