#-----------
# IMPORTS
#-----------

from pathlib import Path
import sys
import pandas as pd

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.ml.atom_features import get_atom_feature_vector

from rdkit import Chem
from rdkit.Chem import AllChem

# ----------------------------------
# DATASET GENERATION
# Build atom-level feature matrix
# ----------------------------------

compounds = get_all_compounds()

rows = []

for compound in compounds:

    compound_name = compound[1]
    smiles = compound[3]

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
            continue

    AllChem.ComputeGasteigerCharges(mol)

    for atom in mol.GetAtoms():

        vector = get_atom_feature_vector(atom)

        rows.append([compound_name, 
                     atom.GetIdx(),
                     atom.GetSymbol(),
                     *vector])

columns = [
    "compound_name",
    "atom_index",
    "atom_symbol",
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
    "aromatic_neighbors",
    "single_bonds",
    "double_bonds",
    "triple_bonds",
    "gasteiger_charge",
    "mean_neighbor_charge",
    "max_neighbor_charge",
    "min_neighbor_charge"
]

df = pd.DataFrame(rows, columns=columns)

print("\nDataset Shape:")
print(df.shape)

# ----------------------------------
# ELECTRONIC FEATURE ANALYSIS
# ----------------------------------

print("\nElectronic Features:")
print(df[["gasteiger_charge",
          "mean_neighbor_charge",
          "max_neighbor_charge",
          "min_neighbor_charge"]].describe())

# ----------------------------------
# ELECTRONIC POLARITY
# ----------------------------------

df["charge_spread"] = (
     df["max_neighbor_charge"]
     -
     df["min_neighbor_charge"]
)

print("\nCharge Spread Statistics:")

print(
     df["charge_spread"]
     .describe()
)

print("\nTop 20 Most Polarized Atoms:")

print(
     df[
          [
               "compound_name",
               "atom_symbol",
               "gasteiger_charge",
               "charge_spread",
               "neighbor_o",
               "neighbor_n",
               "is_aromatic"
          ]
     ]
     .sort_values("charge_spread",
                  ascending=False)
                  .head(20)
)

print(
     df.groupby("atom_symbol")[
          "charge_spread"
     ].describe()
)

df["charge_asymmetry"] = abs(
     df["gasteiger_charge"]
     -
     df["mean_neighbor_charge"])

print(
     df["charge_asymmetry"]
     .describe())

print(
     df[
          [
               "compound_name",
               "atom_symbol",
               "gasteiger_charge",
               "mean_neighbor_charge",
               "charge_asymmetry"
          ]
     ]
     .sort_values("charge_asymmetry",
                  ascending=False)
                  .head(20)
)

print(
     df.groupby("atom_symbol")[
          "charge_asymmetry"
     ].describe()
)

print(
     df.groupby("atom_symbol") [
          "charge_asymmetry"
     ].describe()
)

print(
     df[
          [
               "compound_name",
               "atom_symbol",
               "gasteiger_charge",
               "charge_asymmetry",
               "neighbor_o",
               "neighbor_n",
               "is_aromatic"
          ]
     ]
     .sort_values("charge_asymmetry",
                  ascending=False)
                  .head(50)
)