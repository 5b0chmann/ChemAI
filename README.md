# ChemAI

## Current Version
**v0.8.4.3 Local Dipole Analysis**

## Current Objective

Build machine-learning-ready representations of atomic, electronic, and chemical environments as a foundation for future spectroscopy and molecular property prediction.

## Overview

ChemAI is a cheminformatics and machine learning project focused on understanding molecular structure, electronic environments, atomic environments, and spectroscopy.

The project combines:

- RDKit cheminformatics
- Electronic structure descriptors
- Unsupervised machine learning
- Spectroscopic feature engineering
- Future graph-based deep learning

---

## Roadmap

## v0.8.4.3 Key Results

- 3D molecular conformer generation
- MMFF geometry optimization
- Local atomic dipole vector calculation
- Gasteiger charge difference modeling
- local_dipole_x descriptor
- local_dipole_y descriptor
- local_dipole_z descriptor
- local_dipole_magnitude descriptor
- Dipole Space foundations
- 621 local dipole environments analyzed
- Dipole feature dataset generation
- Integration with QSAR descriptors
- Foundation for Electronic Space vs Lipophilicity analysis

---

### Discovered Chemical Environments

| Cluster | Chemical Environment |
|----------|---------------------|
| 0 | Aromatic Carbon |
| 1 | Aliphatic sp³ Atom |
| 2 | Electron-Rich Heteroatom |
| 3 | Heteroatom-Adjacent Carbon |
| 4 | Carbonyl Carbon |
| 5 | Saturated Ring Atom |
| 6 | Carbonyl Oxygen |
| 7 | Activated Aromatic / Heteroaromatic |

---

### Data Acquisition

✅ v0.1 RSC API Integration

✅ v0.2 Database Foundations

---

### Molecular Representation

✅ v0.3 RDKit Feature Engineering

✅ v0.4 Dataset Builder

✅ v0.5 Molecular Descriptor Analysis

---

### Spectroscopy

✅ v0.6 Spectroscopy Foundations

- SMARTS-based functional group detection
- IR band assignment library
- Intensity modelling
- Peak shape modelling
- Pseudo IR spectrum generation

---

### Machine Learning Foundations

✅ v0.7.1 Atom Environment Features

- Atom-level feature engineering
- Ring-size detection
- Bond-type features
- Aromatic neighbor features
- Atom feature matrix generation

✅ v0.7.2 Electronic Environment Features

- Gasteiger charges
- Neighbor charge descriptors
- Electronic environment analysis
- Charge-aware feature vectors

✅ v0.7.3 PCA Environment Analysis

- Raw PCA
- Scaled PCA
- PCA loadings
- Electronic environment visualization
- Atomic environment outlier detection

✅ v0.8.0 Chemical Environment Discovery

- KMeans clustering
- Cluster center analysis
- Atomic environment classification
- Automatic cluster annotation
- Chemical environment discovery

✅ v0.8.1 Molecular Cluster Fingerprints

- Compound-level cluster fingerprints
- Environment frequency vectors
- Molecule-level representations
- Cluster frequency matrix generation
- Molecule-level chemical environment profiles
- Fingerprint CSV export

✅ v0.8.2 Molecular Similarity Analysis

- Cosine similarity matrix
- Compound similarity ranking
- Fingerprint comparison
- Chemical space analysis
- Similarity matrix export

✅ v0.8.3 Chemical Space Visualization

- Molecular PCA
- Chemical space projection
- Molecular fingerprint heatmaps
- Similarity heatmaps
- Chemical space exploration

✅ v0.8.4 QSAR Foundations

- QSAR dataset generation
- Molecular Weight prediction
- LogP prediction
- TPSA prediction
- Linear Regression baseline models
- Random Forest baseline models
- Model comparison

✅ v0.8.4.1 Electronic Environment Analysis

- charge_spread descriptor
- charge_asymmetry descriptor
- Electronic polarity analysis
- Identification of highly polarized atoms
- Identification of highly asymmetric atoms
- Exploration of local electronic environments
- Foundation for future NMR-related descriptors

✅ v0.8.4.2 Electronic Space Analysis

- Electronic PCA
- Electronic space projection
- charge_spread analysis
- charge_asymmetry analysis
- Electronic class discovery
- Separation of polarized and electronically distinct environments
- First electronic environment mapping

✅ v0.8.4.3 Local Dipole Analysis

- 3D conformer generation
- MMFF geometry optimization
- Local atomic dipole vectors
- Charge difference dipole model
- local_dipole_x
- local_dipole_y
- local_dipole_z
- local_dipole_magnitude
- Dipole feature extraction
- Dipole Space foundations
- Export of local_dipole_features.csv

---

### Molecular Machine Learning

🟡 v0.8.5 Dataset Expansion

Progress:

✅ Phase A – Cardiovascular Drugs

- ACE inhibitors
- Sartans
- Beta blockers

Current Dataset:

- 41 pharmaceutical compounds
- 890 atomic environments

Planned:

- CNS library
- Antibiotics
- Antidiabetics
- Antipsychotics
- Benzodiazepines
- Opioids
- Expanded chemical diversity

🟡 v0.8.5.1 Loader Hardening

Planned:

- Retry handling for HTTP 429
- CAS-based duplicate detection
- Request monitoring
- More robust RSC synchronization

---

### Deep Learning

⬜ v0.9 Neural Networks

Planned:

- Dense neural networks
- Learned molecular representations

⬜ v1.0 Graph Neural Networks

Planned:

- Molecular graph representations
- Message passing architectures
- Learned electronic environments
- Spectral prediction from molecular graphs

---

## Current Pipeline

```text
SMILES
↓
RDKit Molecule
↓
3D Conformer
↓
MMFF Optimization
↓
Atom Features
↓
Electronic Features
↓
charge_spread
↓
charge_asymmetry
↓
Electronic Classes
↓
Electronic PCA
↓
Electronic Space
↓
Local Dipoles
↓
Dipole Space
↓
Chemical Environment Classes
↓
Molecular Cluster Fingerprints
↓
Similarity Analysis
↓
Chemical Space Visualization
↓
Machine Learning
↓
Lipophilicity Analysis
↓
Future NMR Prediction
```
