# ----------------------------------
# DATASET
# ----------------------------------

from pathlib import Path
import sys

import pandas as pd

from rdkit import Chem
from rdkit.Chem import Descriptors

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.ml.cluster_fingerprints import(
    build_compound_cluster_fingerprints)

# ----------------------------------
# DATASET GENERATION
# Compound_level QSAR dataset
# ----------------------------------

compounds = get_all_compounds()

rows = []

for compound in compounds:

    compound_name = compound[1]
    smiles = compound[3]

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        continue

    molecular_weight = Descriptors.MolWt(mol)

    rows.append([compound_name,
                 smiles,
                 molecular_weight
                 ])

columns = [
    "compound_name",
    "smiles",
    "molecular_weight"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

# ----------------------------------
# DATASET OVERVIEW
# ----------------------------------

print(df.head())

print("\nShape:")
print(df.shape)

print("\nMolecular Weight Statistics:")
print(
    df["molecular_weight"]
    .describe()
)


# ----------------------------------
# TARGET GENERATION
# Molecular properties for QSAR
# ----------------------------------

df["logP"] = df["smiles"].apply(
    lambda s: Descriptors.MolLogP(
        Chem.MolFromSmiles(s)
    )
)

df["tpsa"] = df["smiles"].apply(
    lambda s: Descriptors.TPSA(
        Chem.MolFromSmiles(s)
    )
)

print("\nQSAR Target Overview:")

print(
    df[[
        "compound_name",
        "molecular_weight",
        "logP",
        "tpsa"
    ]]
)

print("\nQSAR Target Statistics:")

print(
    df[["molecular_weight",
        "logP",
        "tpsa"
        ]].describe()
)
# ----------------------------------
# MOLECULAR FINGERPRINTS
# QSAR feature matrix
# ----------------------------------

compound_clusters = (
    build_compound_cluster_fingerprints()
)

print("\nCompound Cluster Fingerprints:")
print(compound_clusters.head())

print("\nFingerprint Shape:")
print(compound_clusters.shape)

# ----------------------------------
# LINEAR REGRESSION
# ----------------------------------

print("\n")
print("=" * 80)
print("LINEAR REGRESSION")
print("=" * 80)

# Features
X = compound_clusters

# Target
y = df["molecular_weight"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

r2 = r2_score(
    y_test,
    predictions
)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nMolecular Weight Prediction")

print(f"R² Score: {r2:.3f}")
print(f"MAE: {mae:.3f}")

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\nPrediction Results:")
print(results.round(3))

# ----------------------------------
# RANDOM FOREST
# ----------------------------------

print("\n")
print("=" * 80)
print("RANDOM FOREST")
print("=" * 80)

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)

rf_r2 = r2_score(
    y_test,
    rf_predictions
)

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)

print("\nMolecular Weight Prediction")

print(f"R² Score: {rf_r2:.3f}")
print(f"MAE: {rf_mae:.3f}")

rf_results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": rf_predictions
})

print("\nPrediction Results:")
print(rf_results.round(3))

# ----------------------------------
# MODEL COMPARISON
# ----------------------------------

print("\n")
print("=" * 80)
print("MODEL COMPARISON")
print("=" * 80)

comparison = pd.DataFrame({
    "Model": ["Linear Regression",
              "Random Forest"],
    "R2": [r2,
            rf_r2],
    "MAE": [mae,
            rf_mae]
})

print(comparison.round(3))

# ----------------------------------
# LINEAR REGRESSION
# LogP Prediction
# ----------------------------------

print("\n")
print("=" * 80)
print("LINEAR REGRESSION - LOGP")
print("=" * 80)

y = df["logP"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train, 
    y_train
)

predictions = model.predict(
    X_test
)

logp_r2 = r2_score(
    y_test,
    predictions 
)

logp_mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nLogP Prediction")
print(f"R² Score: {logp_r2:.3f}")
print(f"MAE: {logp_mae:.3f}")

logp_results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\nPrediction Results:")
print(logp_results.round(3))

# ----------------------------------
# LINEAR REGRESSION
# TPSA Prediction
# ----------------------------------

print("\n")
print("=" * 80)
print("LINEAR REGRESSION - TPSA")
print("=" * 80)

y = df["tpsa"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train, 
    y_train
)

predictions = model.predict(
    X_test
)


tpsa_r2 = r2_score(
    y_test,
    predictions
)

tpsa_mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nTPSA Prediction")
print(f"R² Score: {tpsa_r2:.3f}")
print(f"MAE: {tpsa_mae:.3f}")

tpsa_results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\nPrediction Results:")
print(tpsa_results.round(3))

# ----------------------------------
# MODEL COMPARISON
# ----------------------------------

print("\nDataset Size:")
print(X.shape)

print("\nTraining Samples:")
print(len(X_train))

print("\nTest Samples:")
print(len(X_test))

# ----------------------------------
# EXPORT
# ----------------------------------