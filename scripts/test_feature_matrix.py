from pathlib import Path
import sys
import pandas as pd
from rdkit import Chem
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.ml.atom_features import get_atom_feature_vector

compounds = get_all_compounds()

rows = []

for compound in compounds:

    compound_name = compound[1]
    smiles = compound[3]

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        continue

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
    "triple_bonds"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("atom_feature_matrix.csv", index=False)

print(df.head())

print("\nShape:")
print(df.shape)

print("\nAtom counts per compound:")
print(df.groupby("compound_name").size().sort_values(ascending=False))

print("\nAtomic Numbers:")
print(df["atomic_number"].value_counts())

print("\nHybridization:")
print(df["hybridization"].value_counts())

print("\nRing Sizes:")
print(df["ring_size"].value_counts())

print("\nAromatic Atoms:")
print(df["is_aromatic"].value_counts())

print("\nAtoms in Rings:")
print(df["is_in_ring"].value_counts())

print("\nNeighbors Oxygen:")
print(df["neighbor_o"].value_counts())

print("\nNeighbors Nitrogen:")
print(df["neighbor_n"].value_counts())

print(df.describe())

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
]

print(
    df.groupby(feature_columns)
      .size()
      .sort_values(ascending=False)
      .head(20)
)

env_counts = (
    df.groupby(feature_columns)
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False))

print(env_counts.head(20))

# PCA Analyse - Welche Features dominieren?

X = df[feature_columns]

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)
df["PC1"] = X_pca[:,0]
df["PC2"] = X_pca[:, 1]

loadings = pd.DataFrame(pca.components_.T, 
                        columns=["PC1", "PC2"],
                        index=feature_columns)

print(loadings)

print(X_pca[:10])

# ML-Plot
colors = {"C": "black",
          "O": "red",
          "N": "blue",
          "Cl": "green"}

plt.figure(figsize=(10,8))

for symbol in df["atom_symbol"].unique():

    mask = df["atom_symbol"] == symbol

    plt.scatter(X_pca[mask, 0],
                X_pca[mask, 1],
                label=symbol,
                alpha=0.7,
                color=colors.get(symbol, "gray"))

scatter = plt.scatter(X_pca[:,0],
                      X_pca[:,1],
                      c=df["is_aromatic"],
                      cmap="coolwarm",
                      alpha=0.7)
plt.xlabel("PC1")
plt.ylabel("PC2")

plt.title("PCA of Atomic Electronic Enviroments")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

scatter = plt.scatter(X_pca[:,0],
                      X_pca[:,1],
                      c=df["is_aromatic"],
                      cmap="coolwarm",
                      alpha=0.7)

interesting = df[(df["PC1"] > 1) & (df["PC1"] < 4) & (df["PC2"] >1)]

print(interesting[["compound_name",
    "atom_index",
    "atom_symbol",
    "is_aromatic",
    "hybridization",
    "neighbor_c",
    "neighbor_n",
    "neighbor_o",
    "neighbor_halogen",
    "aromatic_neighbors",
    "single_bonds",
    "double_bonds",
    "PC1",
    "PC2"]])

plt.xlabel("PC1")
plt.ylabel("PC2")

plt.title("PCA of Electronic Eviroments \n Colored by Aromaticity")

cbar = plt.colorbar(scatter)
cbar.set_label("Aromatic (0 = No, 1 = Yes)")

plt.grid(True)

plt.tight_layout()

plt.show()