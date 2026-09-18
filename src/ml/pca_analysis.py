#-----------
# IMPORTS
#-----------
from pathlib import Path
import sys

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import pandas as pd

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.ml.electronic_properties import(build_electonic_dataset)

# ----------------------------------
# DATASET
# ----------------------------------

df = build_electonic_dataset()

print("\nDataset Shape:")
print(df.shape)

# ----------------------------------
# ELECTRONIC FEATURES
# ----------------------------------

electronic_features = [
    "gasteiger_charge",
    "mean_neighbor_charge",
    "max_neighbor_charge",
    "min_neighbor_charge",
    "charge_spread",
    "charge_asymmetry"
]

# ----------------------------------
# STANDARDIZATION
# ----------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(
    df[electronic_features]
)

# ----------------------------------
# ELECTRONIC PCA
# ----------------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(
    X_scaled
)

df["PC1"] = X_pca[:, 0]
df["PC2"] = X_pca[:, 1]

# ----------------------------------
# PCA LOADINGS
# ----------------------------------

loadings = pd.DataFrame(
    pca.components_.T,
    columns=["PC1", "PC2"],
    index=electronic_features
)

print("\nElectronic PCA Loadings:")

print(
    loadings.round(3)
)

print("\nExplained Variance Ratio:")

print(
    pca.explained_variance_ratio_
)

print("\nFirst 20 PCA Coordinates:")

print(
    df[
        [
            "atom_symbol",
            "electronic_class",
            "PC1",
            "PC2"
        ]
    ]
    .head(20)
)

# ----------------------------------
# ELECTRONIC SPACE
# ----------------------------------

colors = {
    "neutral": "gray",
    "highly_polarized": "red",
    "electronically_distinct": "blue",
    "electronic_hotspot":"purple"
}

plt.figure(figsize=(12, 8))

for electronic_class in df[
    "electronic_class"
].unique():

    mask = (
        df["electronic_class"]
        == electronic_class
    )

    plt.scatter(
        df.loc[mask, "PC1"],
        df.loc[mask, "PC2"],
        label=electronic_class,
        alpha=0.7,
        color=colors.get(
            electronic_class,
            "black"
        )
    )

plt.xlabel("PC1")

plt.ylabel("PC2")

plt.title(
    "Electronic Space of Atomic Environments"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()