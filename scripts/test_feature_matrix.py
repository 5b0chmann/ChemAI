from pathlib import Path
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.ml.atom_features import get_atom_feature_vector

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

# ----------------------------------
# BASIC DATASET STATISTICS
# ----------------------------------

df = pd.DataFrame(rows, columns=columns)

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

# ----------------------------------
# ELECTRONIC FEATURE ANALYSIS
# ----------------------------------

print(df.describe())

print("\nElectronic Features:")
print(df[["gasteiger_charge",
          "mean_neighbor_charge",
          "max_neighbor_charge",
          "min_neighbor_charge"]].describe())

# ----------------------------------
# ENVIRONMENT FREQUENCY ANALYSIS
# Most common atomic environments
# ----------------------------------

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

# ----------------------------------
# PCA WITHOUT SCALING
# Topology-dominated PCA
# ----------------------------------

X = df[feature_columns]

pca_raw = PCA(n_components=2)

X_pca_raw = pca_raw.fit_transform(X)

df["PC1_raw"] = X_pca_raw[:,0]
df["PC2_raw"] = X_pca_raw[:, 1]

loadings_raw = pd.DataFrame(
     pca_raw.components_.T,
     columns=["PC1_raw", "PC2_raw"],
     index=feature_columns)

print("\nRaw PCA Loadings:")
print(loadings_raw)

# ----------------------------------
# PCA WITH STANDARD SCALING
# Topology + Electronic Features
# ----------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(df[feature_columns])

pca_scaled = PCA(n_components=2)

X_pca_scaled = pca_scaled.fit_transform(X_scaled)

df["PC1_scaled"] = X_pca_scaled[:,0]
df["PC2_scaled"] = X_pca_scaled[:, 1]

# ----------------------------------
# PCA LOADINGS ANALYSIS
# Which features drive the components?
# ----------------------------------

loadings_scaled= pd.DataFrame(pca_scaled.components_.T,
                              columns=["PC1_scaled", "PC2_scaled"],
                              index=feature_columns)

print("\nScaled PCA Loadings:")
print(loadings_scaled)
print("\nExplained Variance Ratio:")
print(pca_scaled.explained_variance_ratio_)


print("\nFirst 10 PCA Coordinates:")
print(X_pca_scaled[:10])

# ----------------------------------
# PCA VISUALIZATION
# Atomic environment projection
# ----------------------------------

colors = {"C": "black",
          "O": "red",
          "N": "blue",
          "Cl": "green"}

plt.figure(figsize=(10,8))

for symbol in df["atom_symbol"].unique():

    mask = df["atom_symbol"] == symbol

    plt.scatter(X_pca_scaled[mask, 0],
                X_pca_scaled[mask, 1],
                label=symbol,
                alpha=0.7,
                color=colors.get(symbol, "gray"))

scatter = plt.scatter(X_pca_scaled[:,0],
                      X_pca_scaled[:,1],
                      c=df["is_aromatic"],
                      cmap="coolwarm",
                      alpha=0.7)
plt.xlabel("PC1_scaled")
plt.ylabel("PC2_scaled")

plt.title("PCA of Atomic Electronic Environments")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

plt.figure(figsize=(10,8))

scatter = plt.scatter(X_pca_scaled[:,0],
                      X_pca_scaled[:,1],
                      c=df["is_aromatic"],
                      cmap="coolwarm",
                      alpha=0.7)

# ----------------------------------
# PCA OUTLIER ANALYSIS
# Interesting atomic environments
# ----------------------------------

interesting = df[
     (df["PC1_scaled"] > 1)
      & (df["PC1_scaled"] < 4)
      & (df["PC2_scaled"] >1)]

print("\nInteresting Atoms:")
print(f"Count: {len(interesting)}")

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
    "PC1_scaled",
    "PC2_scaled"]])

interesting_neg = df[
     (df["PC1_scaled"] < -2)
     & (df["PC2_scaled"] < 0)
]

print(interesting_neg[["compound_name",
                       "atom_symbol",
                       "gasteiger_charge",
                       "neighbor_o",
                       "neighbor_n"]])

plt.xlabel("PC1_scaled")
plt.ylabel("PC2_scaled")

plt.title("PCA of Electronic Evironments \n Colored by Aromaticity")

cbar = plt.colorbar(scatter)
cbar.set_label("Aromatic (0 = No, 1 = Yes)")

plt.grid(True)

plt.tight_layout()

plt.show()

# ----------------------------------
# KMEANS CLUSTERING
# Automatic environment discovery
# ----------------------------------

kmeans = KMeans(n_clusters=8, random_state=42, n_init=10)

clusters = kmeans.fit_predict(X_scaled)

df["cluster"] = clusters

cluster_names ={
     0: "Aromatic Carbon",
     1: "Aliphatic sp3 Atom",
     2: "Electron-Rich Heteroatom",
     3: "Heteroatom-Adjacent Carbon",
     4: "Carbonyl Carbon",
     5: "Saturated Ring Atom",
     6: "Carbonyl Oxygen",
     7: "Activated Aromatic/Heteroaromatic"
}
df["cluster_name"] = df["cluster"].map(cluster_names)

print("\nCluster Sizes:")
print(df["cluster"].value_counts())

print("\nCluster Distribution:")
print(df["cluster_name"].value_counts())

print("\nCluster Summary:")

cluster_summary = (df.groupby("cluster")[["gasteiger_charge",
                                         "hybridization",
                                         "neighbor_o",
                                         "neighbor_n",
                                         "is_aromatic",
                                         "ring_size"]].mean())

print(cluster_summary)

print("\nAtom Types per Cluster:")

print(df.groupby("cluster")["atom_symbol"].value_counts())

# ----------------------------------
# Molecular Cluster Fingerprints
# ----------------------------------

compound_clusters = (df.groupby(["compound_name", "cluster_name"]).size().unstack(fill_value=0))

print("\n Compound Cluster Fingerprints:")
print(compound_clusters)

compound_clusters.to_csv("compound_cluster_fingerprints.csv")

# ----------------------------------
# CLUSTER INTERPRETATION
# Example atoms from each cluster
# ----------------------------------

for c in sorted(df["cluster"].unique()):

     print("\n" + "=" * 60)
     print(f"CLUSTER {c}")
     print("=" * 60)

     sample = df[df["cluster"] == c][["compound_name", 
                                      "atom_index",
                                      "atom_symbol",
                                      "gasteiger_charge",
                                      "hybridization",
                                      "neighbor_o",
                                      "neighbor_n",
                                      "is_aromatic",
                                      "ring_size"]]

     print(sample.head(20))

# ----------------------------------
# CLUSTER CENTERS
# ----------------------------------

centers = pd.DataFrame(kmeans.cluster_centers_,
                       columns=feature_columns)

centers_original = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_),
                                columns=feature_columns)

pd.set_option("display.max_columns", None)

print("\nCluster Center (Scaled)")
print(centers.round(3))

print("\nCluster Center (Original Scale)")
print(centers_original.round(3))

for cluster_id in centers_original.index:
     print("\n" + "=" * 60)
     print(f"CLUSTER {cluster_id}")
     print("=" * 60)

     center = centers_original.loc[cluster_id]

     print(center.round(2))


centers_original = centers_original.reset_index()
centers_original.rename(columns={"index": "cluster"}, inplace=True)

centers_original.to_csv("cluster_center.csv", index=False)

# ----------------------------------
# KMEANS VISUALIZATION
# Cluster projection in PCA space
# ----------------------------------

plt.figure(figsize=(10,8))

scatter = plt.scatter(
     X_pca_scaled[:, 0],
     X_pca_scaled[:, 1],
     c=df["cluster"],
     cmap="tab10",
     alpha=0.7)

plt.xlabel("PC1_scaled")
plt.ylabel("PC2_scaled")

plt.title("KMeans Clusters of Aromatic Environments")

plt.colorbar(scatter)

plt.grid(True)

plt.tight_layout()

plt.show()

interesting_neg = df[
     (df["PC1_scaled"] < -2)
     &(df["PC2_scaled"] < 0)
]

# ----------------------------------
# EXPORT
# ----------------------------------

df.to_csv("atom_feature_matrix_with_pca.csv", index=False)
