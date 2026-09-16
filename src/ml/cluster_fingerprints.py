from pathlib import Path
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.ml.atom_features import get_atom_feature_vector

def build_compound_cluster_fingerprints():

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

            rows.append([
                compound_name,
                atom.GetIdx(),
                atom.GetSymbol(),
                *vector
            ])

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

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    feature_columns = [
        "degree",
        "valence",
        "hybridization",
        "is_aromatic",
        "is_in_ring",
        "ring_size",
        "neighbor_c",
        "neighbor_n",
        "neighbor_o",
        "aromatic_neighbors",
        "single_bonds",
        "double_bonds",
        "gasteiger_charge",
        "mean_neighbor_charge",
        "max_neighbor_charge",
        "min_neighbor_charge"
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(
        df[feature_columns]
    )

    kmeans = KMeans(
        n_clusters=8,
        random_state=42,
        n_init=10
    )

    df["cluster"] = kmeans.fit_predict(
        X_scaled
    )

    cluster_names = {
        0: "Aromatic Carbon",
        1: "Aliphatic sp3 Atom",
        2: "Electron-Rich Heteroatom",
        3: "Heteroatom-Adjacent Carbon",
        4: "Carbonyl Carbon",
        5: "Saturated Ring Atom",
        6: "Carbonyl Oxygen",
        7: "Activated Aromatic/Heteroaromatic"
    }

    df["cluster_name"] = df[
        "cluster"
    ].map(cluster_names)

    compound_clusters = (
        df.groupby(
            ["compound_name", "cluster_name"]
        )
        .size()
        .unstack(fill_value=0)
    )

    return compound_clusters

if __name__ == "__main__":

    fingerprints = (
        build_compound_cluster_fingerprints()
    )

    print("\nFingerprints")
    print(fingerprints.head())
