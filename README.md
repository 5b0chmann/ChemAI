# ChemAI

ChemAI is a cheminformatics and machine learning project focused on pharmaceutical compounds, molecular descriptors, and structure-property relationships.

## Current Version

**v0.5 Molecular Descriptor Analysis**

## Project Roadmap

### Phase 1 – Data Acquisition
- ✅ v0.1 RSC API Integration
- ✅ v0.2 SQLite Database
- ✅ Compound Registry
- ⏸ Google Drive Synchronization (deferred)

### Phase 2 – Descriptor Analysis
- ✅ v0.3 RDKit Feature Engineering
- ✅ v0.4 Dataset Builder
- ✅ v0.5 Molecular Descriptor Analysis

### Phase 3 – Machine Learning
- ⬜ Random Forest Baseline
- ⬜ Artificial Neural Network (ANN)
- ⬜ GPU Acceleration

### Phase 4 – Deep Learning
- ⬜ Molecular Graph Generation
- ⬜ Graph Neural Networks (GNN)
- ⬜ Model Comparison

---

## Dataset

Current dataset:

- 20 curated pharmaceutical compounds
- Analgesics
- Antiepileptics
- Anesthetics

Stored in:

- `Data/chemai.db`
- `Data/compound_descriptors.csv`

---

## Implemented Features

### Data Layer

- RSC API integration
- SQLite storage
- Compound registry
- Automated compound loading

### RDKit Descriptor Pipeline

Calculated descriptors:

- Molecular Weight (MolWt)
- LogP
- TPSA
- HDonors
- HAcceptors
- Rotatable Bonds
- Ring Count
- Heavy Atom Count
- Hetero Atom Count
- Valence Electrons
- FractionCSP3

### Analysis

- Descriptor DataFrame generation
- CSV export
- Class-based statistical analysis
- Correlation analysis
- Outlier detection

---

## Key Findings (v0.5)

### Anesthetics

- Highest average LogP
- Lowest average TPSA
- Relatively homogeneous descriptor profile

### Antiepileptics

- Highest average TPSA
- Highest average FractionCSP3
- Most structurally heterogeneous class

### Analgesics

- More aromatic character
- Lower average FractionCSP3

### Stereochemistry

The following stereoisomer pairs produced identical classical 2D RDKit descriptors:

- (S)-Ibuprofen / (R)-Ibuprofen
- (+)-Etomidate / (-)-Etomidate

This demonstrates the limitations of traditional 2D descriptor approaches.

---

## Next Release

### v0.6 Spectroscopy Foundations

Planned topics:

- Functional group detection
- IR-relevant features
- NMR-relevant features
- Spectroscopic interpretation

---

## Technologies

- Python
- RDKit
- SQLite
- Pandas
- NumPy
- Scikit-learn