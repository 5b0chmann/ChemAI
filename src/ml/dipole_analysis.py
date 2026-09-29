"""
ChemAI v0.8.4.4
Dipole Space Analysis

Purpose:
Analyse atom-level and 
molecule-level dipole features.

Author:
ChemAI
"""

import pandas as pd


#---------------
# Load Dataset
#---------------

df = pd.read_csv(
    "data/dipole/local_dipole_features.csv"
)

print("\nDataset Shape:")
print(df.shape)

#---------------------
# Global Statistics
#---------------------

print("\nDipole Statistics:")
print(
    df["local_dipole_magnitude"]
    .describe()
)

#---------------------
# Atom Type Analysis
#---------------------

print("\nMean Dipole by Atom Type:")

atom_summary = (
    df.groupby("atom_symbol")
    ["local_dipole_magnitude"]
    .mean()
    .sort_values(
        ascending=False
    )
)

print(atom_summary)

#---------------------
# Top Atomic Dipoles
#---------------------

print("\nTop 20 Atomic Dipoles:")

top_atoms = (
    df.sort_values(
        "local_dipole_magnitude",
        ascending=False
    )
    .head(20)
)

print(
    top_atoms[
        [
            "compound_name",
            "atom_symbol",
            "local_dipole_magnitude"
        ]
    ]
)

#-------------------------
# Molecule-Level Dipoles
#-------------------------

print("\nMean Molecular Dipole:")

molecule_summary = (
    df.groupby(
        "compound_name"
    )
    [
        "local_dipole_magnitude"
    ]
    .mean()
    .sort_values(
        ascending=False
    )
)

print(
    molecule_summary
    .head(20)
)

#------------------------
# Molecule Statistics
#------------------------

molecule_stats = (
    df.groupby("compound_name")
    .agg(
        mean_dipole=(
            "local_dipole_magnitude",
            "mean"
        ),
        max_dipole=(
            "local_dipole_magnitude",
            "max"
        ),
        std_dipole=(
            "local_dipole_magnitude",
            "std"
        ),
        log_p=(
            "log_p",
            "first"
        ),
        tpsa=("tpsa",
              "first"
        )
        
    )
    .sort_values(
        by="mean_dipole",
        ascending=False
    )
)

print(
    "\nMean / Max / Std Dipoles:"
)

print(
    molecule_stats
)

#--------------------------------------
# Full Descriptor Correlations Matrix
#--------------------------------------


descriptor_cols =  [
            "mean_dipole",
            "max_dipole",
            "std_dipole",
            "log_p",
            "tpsa"
        ]
print(
    "\nFull Descriptor Correlation Matrix:")

print(
    molecule_stats[
        descriptor_cols
    ].corr()
)

print(
    "\nDipole Space Correlations:"
)

print(molecule_stats.corr()[
    ["mean_dipole",
     "max_dipole",
     "std_dipole"
     ]
]
.sort_values(
    by="mean_dipole",
    ascending=False
))

#---------------------
# LogP Correlation
#---------------------

corr_df = (
    df.groupby(
        "compound_name"
    )
    [
        [
            "local_dipole_magnitude",
            "log_p"
        ]
    ]
    .mean()
)

print("\nMolecule Summary:")

print(
    corr_df.sort_values(
        "local_dipole_magnitude",
        ascending=False
    )
)

print("\nDipole vs LogP Correlation:")
print(
    corr_df.corr()
)

# strongest molecules

print("\nStrongest Molecules")
print(
    corr_df.sort_values(
        "log_p"
    )
)

