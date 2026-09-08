from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Descriptors
import sys
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.data.compound_registry import compound_registry

def calculate_descriptors(smiles):
    """Calculate RDKit descriptors for a SMILES string."""

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return {"mol_wt": Descriptors.MolWt(mol),
            "log_p": Descriptors.MolLogP(mol),
            "tpsa": Descriptors.TPSA(mol),
            "h_donors": Descriptors.NumHDonors(mol),
            "h_acceptors": Descriptors.NumHAcceptors(mol),
            "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
            "ring_count": Descriptors.RingCount(mol),
            "heavy_atoms": Descriptors.HeavyAtomCount(mol),
            "hetero_atoms": Descriptors.NumHeteroatoms(mol),
            "valence_electrons": Descriptors.NumValenceElectrons(mol),
            "fraction_csp3": Descriptors.FractionCSP3(mol)}

compounds = get_all_compounds()

print(f"Number of compounds: {len(compounds)}")

descriptor_dataset = []

for compound in compounds:
    name = compound[1]
    smiles = compound[3]
    descriptors = calculate_descriptors(smiles)
    if descriptors is None:
        print(f"Failed: {name}")
        continue

    descriptor_row = {"name": name,
                     "class": compound_registry[name]["class"],
                     "smiles": smiles,
                     **descriptors}

    descriptor_dataset.append(descriptor_row)
df = pd.DataFrame(descriptor_dataset)

summary = (df.groupby("class").agg({"mol_wt": ["mean", "min", "max", "std"],
                                    "log_p": ["mean", "min", "max", "std"],
                                    "tpsa": ["mean", "min", "max", "std"],
                                    "fraction_csp3": ["mean", "min", "max", "std"]}))

print(summary)

correlation = df[["mol_wt", "log_p", "tpsa", "fraction_csp3", "rotatable_bonds", "ring_count"]].corr()
print(correlation)

def show_extremes(df, column):
    print(f"\nHighest {column}")
    print("=" * 40)

    print(df[["name", "class", column]].sort_values(column, ascending=False))

    print(f"\nLowest {column}")
    print("=" * 40)

    print(df[["name", "class", column]].sort_values(column, ascending=True))



show_extremes(df, "log_p")
show_extremes(df, "tpsa")
show_extremes(df, "fraction_csp3")
