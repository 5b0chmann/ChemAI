""" 
ChemAI v0.8.4.3
Local Dipol Analysis

Purpose:
Calculate local atomic dipole vectors from 
Gasteiger charges and 3D molecular geometry.

Outputs:
- local_dipole_x
- local_dipole_y
- local_dipole_z
- local_dipole_magnitude

Author:
ChemAI
"""

import numpy as np
import pandas as pd

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdPartialCharges

from pathlib import Path


#-----------------------
# Molecule Preparation
#-----------------------

def prepare_molecule(smiles: str):
    """
    Generate 3D coordinates and Gasteiger charges.
    """

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    mol = Chem.AddHs(mol)

    # Generate 3D coordinates
    status = AllChem.EmbedMolecule(
        mol,
        randomSeed = 42
    )

    if status != 0:
        return None

    # Geometry optimization
    AllChem.MMFFOptimizeMolecule(mol)

    # Partial charges
    rdPartialCharges.ComputeGasteigerCharges(mol)

    return mol

#----------------------------
# Local Dipol Calculation
#----------------------------

def calculate_local_dipoles(mol):
    """
    Calculate local dipole vectors
    for every atom in the molecule.
    """

    conf = mol.GetConformer()

    results = []

    for atom in mol.GetAtoms():
        
        atom_idx = atom.GetIdx()

        
        try:
            atom_charge = float(
            atom.GetProp("_GasteigerCharge")
        )

            if np.isnan(atom_charge):
                atom_charge = 0.0

        except Exception:
            atom_charge = 0.0

        atom_pos = np.array(
            conf.GetAtomPosition(atom_idx)
        )

        dipole_vector = np.zeros(3)

        for neighbor in atom.GetNeighbors():

            nbr_idx = neighbor.GetIdx()

            nbr_pos = np.array(
                conf.GetAtomPosition(nbr_idx)
            )

            charge = neighbor.GetProp(
                "_GasteigerCharge"
            )

            try:
                neighbor_charge = float(charge)

                if np.isnan(neighbor_charge):
                    neighbor_charge = 0.0

            except Exception:
                neighbor_charge = 0.0

            direction_vector = (
                nbr_pos - atom_pos
            )

            charge_difference = (
                neighbor_charge
                - atom_charge
            )

            dipole_vector += (
                charge_difference
                * direction_vector
            )

        magnitude = np.linalg.norm(
                dipole_vector
            )

        results.append(
                {
                    "atom_index": atom_idx,
                    "atom_symbol": atom.GetSymbol(),
                    "local_dipole_x": dipole_vector[0],
                    "local_dipole_y": dipole_vector[1],
                    "local_dipole_z": dipole_vector[2],
                    "local_dipole_magnitude": magnitude
                }
            )
    return pd.DataFrame(results)

#----------------------------
# Single Molecule Analysis
#----------------------------

def analyse_smiles(smiles):

    mol = prepare_molecule(smiles)

    if mol is None:
        return None

    return calculate_local_dipoles(mol)

#----------------------------
# Dataset Runner
#----------------------------

def run_dataset(
        input_csv = "data/qsar/compound_descriptors.csv",
        output_csv = "data/dipole/local_dipole_features.csv"
):
    """
    Expected columns:
    
    name
    smiles
    mol_wt
    log_p
    tpsa
    """

    df = pd.read_csv(input_csv)

    all_results = []

    for _, row in df.iterrows():

        compound_name = row["name"]
        smiles = row["smiles"]
        
        print(
            f"Processing: {compound_name}"
        )

        atom_df = analyse_smiles(smiles)

        if atom_df is None:
            print(
                f"Failed: {compound_name}"
            )
            continue
        atom_df["compound_name"] = (
            compound_name
        )

        atom_df["smiles"] = smiles

        atom_df["log_p"] = row["log_p"]

        atom_df["mol_wt"] = row["mol_wt"]
        
        atom_df["tpsa"] = row["tpsa"]

        all_results.append(atom_df)

    if not all_results:

        print(
            "No molecules processed."
        )
        return

    final_df = pd.concat(
        all_results,
        ignore_index=True
    )

    Path(output_csv).parent.mkdir(
        parents = True,
        exist_ok = True
    )

    final_df.to_csv(
        output_csv,
        index=False
    )

    print(
        f"\nSaved: {output_csv}"
    )

    print(
        f"Atoms analysed: {len(final_df)}"
    )

    print(
        "\nDipole Statistics:"
    )

    print(
        final_df[
            "local_dipole_magnitude"
        ].describe()
    )

#----------------------------
# Example
#----------------------------

if __name__ == "__main__":

    # Single molecule test

    smiles = "CC(=O)NC1=CC=C(O)C=C1"

    df = analyse_smiles(smiles)

    print(df.head())

    print(
        "\nTop Dipole Atoms:"
    )

    print(
        df.sort_values(
            "local_dipole_magnitude",
            ascending=False
        ).head(10)
    )

    # Dataset mode

    run_dataset(
        "data/qsar/compound_descriptors.csv",
        "data/dipole/local_dipole_features.csv")
