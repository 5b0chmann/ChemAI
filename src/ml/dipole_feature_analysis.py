"""
ChemAI v0.8.4.5
Dipole Feature Analysis

Purpose:
Identify structural features
associated with high local dipoles.

Author:
ChemAI
"""

import pandas as pd

#---------------------
# Load Datasets
#---------------------

dipole_df = pd.read_csv(
    "data/dipole/local_dipole_features.csv"
)


feature_df = pd.read_csv(
    "data/chemistry/atom_feature_matrix.csv"
)

print("\nDipole Dataset:")
print(dipole_df.shape)

print("\nFeature Dataset:")
print(feature_df.shape)

#---------------------
# Merge Datasets
#---------------------

merge_cols = [
    "compound_name",
    "atom_index"
]

merge_df = pd.merge(
    dipole_df,
    feature_df,
    on=merge_cols,
    how="inner"
)

print(
    (
        merge_df["atom_symbol_x"]
        ==
        merge_df["atom_symbol_y"]
    ).all()
)

merge_df = merge_df.rename(
    columns={"atom_symbol_x": "atom_symbol"}
)

merge_df = merge_df.drop(
    columns=["atom_symbol_y"]
)

print("\nMerged Columns:")
print(merge_df.columns.tolist())

print("\nMerged Dataset:")
print(merge_df.shape)

#---------------------
# Global Statistics
#---------------------

print("\nDipole Statistics:")

print(
    merge_df[
        "local_dipole_magnitude"
    ].describe()
)

#--------------------------
# Hybridization Analysis
#--------------------------

print("\nMean Dipole by Hybridization:")

print(
    merge_df.groupby(
        "hybridization"
    )[
        "local_dipole_magnitude"
    ]
    .mean()
    .sort_values(
        ascending=False
    )
)

#--------------------------
# Aromatic Analysis
#--------------------------

print("\nMean Dipole by Aromaticity:")

print(
    merge_df.groupby(
        "is_aromatic"
    )[
        "local_dipole_magnitude"
    ]
    .mean()
)

#--------------------------
# Ring Analysis
#--------------------------

print("\nMean Dipole by Ring Membership:")

print(
    merge_df.groupby(
        "is_in_ring"
    )[
        "local_dipole_magnitude"
    ]
    .mean()
)

#--------------------------
# Ring Size Analysis
#--------------------------

print(
    "\nMean Dipole by Ring Size:"
)

print(
    merge_df.groupby(
        "ring_size"
    )[
        "local_dipole_magnitude"
    ]
    .mean()
    .sort_values(
        ascending=False
    )
)

#--------------------------
# Neighbor Analysis
#--------------------------

neighbor_features = [
    "neighbor_c",
    "neighbor_n",
    "neighbor_o",
    "neighbor_halogen"
]

for feature in neighbor_features:

    print(
        f"\nMean Dipole by {feature}:"
    )
    
    print(
        merge_df.groupby(
            feature
    )[
        "local_dipole_magnitude"
    ]
    .mean()
)

#--------------------------
# Bond Analysis
#--------------------------

bond_features = [
    "single_bonds",
    "double_bonds",
    "triple_bonds"
]

for feature in bond_features:

    print(
        f"\nMean Dipole by {feature}:"
    )

    print(
        merge_df.groupby(
            feature
        )[
            "local_dipole_magnitude"
    ]
    .mean()
)

#--------------------------
# Correlation Matrix
#--------------------------

correlation_features = [
    "local_dipole_magnitude",
    "atomic_number",
    "degree",
    "formal_charge",
    "valence",
    "hybridization",
    "is_aromatic",
    "is_in_ring",
    "ring_size",
    "num_hydrogens",
    "neighbor_n",
    "neighbor_o",
    "neighbor_c",
    "neighbor_halogen",
    "single_bonds",
    "double_bonds",
    "triple_bonds"
]

corr_df = merge_df[
    correlation_features
].copy()

print(
    "\nFeature Correlation Matrix:"
)

print(
    corr_df.corr(
        numeric_only=True
    )
)

#--------------------------
# Strongest Dipole Atoms
#--------------------------

print(
    "\nTop 30 Dipole Atoms:"
)

print(
    merge_df
    .sort_values(
        "local_dipole_magnitude",
        ascending=False
    )
    [
        [
            "compound_name",
            "atom_symbol",
            "local_dipole_magnitude",
            "hybridization",
            "neighbor_o",
            "neighbor_n",
            "double_bonds"
        ]
    ]
    .head(30)
)

#--------------------------
# Dipole Driver Ranking
#--------------------------

top_features = (
    merge_df[
        [
            "local_dipole_magnitude",
            "neighbor_o",
            "neighbor_n",
            "neighbor_c",
            "double_bonds",
            "single_bonds",
            "is_aromatic",
            "is_in_ring"
        ]
    ]
    .corr()
)

print(
    "\nDipole Driver Ranking:"
)

dipole_drivers = (
    top_features[
        "local_dipole_magnitude"
        ]
        .sort_values(
            ascending=False
        )
)

print()
print(dipole_drivers)