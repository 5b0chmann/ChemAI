# ChemAI

## Current Version
**v0.8.0 Atomic Environment Discovery**

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

## v0.8.0 Key Results

- 20 pharmaceutical compounds analyzed
- 312 atomic environments extracted
- 24 engineered atom-level descriptors
- Electronic environment modelling
- PCA analysis of atomic environments
- KMeans clustering of atomic environments
- Automatic chemical environment annotation
- Discovery of 8 recurring chemical environment classes

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

---

### Molecular Machine Learning

🟡 v0.8.1 Molecular Cluster Fingerprints

Planned:

- Compound-level cluster fingerprints
- Environment frequency vectors
- Molecule-level representations

🟡 v0.8.2 QSAR Foundations

Planned:

- Physicochemical property prediction
- Toxicity prediction
- Activity prediction

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
Atom Features
↓
Electronic Features
↓
Atomic Environment Matrix
↓
PCA
↓
KMeans Clustering
↓
Chemical Environment Classes
↓
Molecular Fingerprints
↓
Machine Learning