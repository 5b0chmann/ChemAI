# ChemAI

ChemAI is a cheminformatics and molecular spectroscopy project focused on pharmaceutical compounds, molecular descriptors, functional groups, and structure-spectrum relationships.

## Current Version

**v0.6 Spectroscopy Foundations**

---

## Project Roadmap

### Phase 1 – Data Acquisition

- ✅ v0.1 RSC API Integration
- ✅ v0.2 SQLite Database
- ✅ Compound Registry

### Phase 2 – Molecular Descriptors

- ✅ v0.3 RDKit Feature Engineering
- ✅ v0.4 Dataset Builder
- ✅ v0.5 Molecular Descriptor Analysis

### Phase 3 – Spectroscopy

- ✅ v0.6 Spectroscopy Foundations
- ⬜ v0.7 NMR Foundations
- ⬜ UV/Vis Foundations

### Phase 4 – Machine Learning

- ⬜ Random Forest Baseline
- ⬜ Artificial Neural Networks
- ⬜ Spectral Feature Learning

### Phase 5 – Deep Learning

- ⬜ Molecular Graph Generation
- ⬜ Graph Neural Networks
- ⬜ Model Comparison

---

## Dataset

Current dataset:

- 20 curated pharmaceutical compounds

Classes:

- Analgesics
- Antiepileptics
- Anesthetics

---

## Technologies

- Python
- RDKit
- Pandas
- NumPy
- Matplotlib
- SQLite
- Scikit-learn

---

## Functional Group Detection

ChemAI uses SMARTS-based pattern matching for functional group recognition.

Implemented groups:

- Aromatic Ring
- Alcohol
- Phenol
- Carboxylic Acid
- Amide
- Amine
- Ester
- Ketone
- Ether
- Aliphatic Ether

---

## IR Spectroscopy Module

ChemAI can assign expected IR bands based on detected functional groups.

Each IR band stores:

- Band assignment
- Wavenumber range
- Intensity
- Shape

Example:

```python
{
    "band": "C=O stretch",
    "range": "1705-1725 cm-1",
    "intensity": "strong",
    "shape": "sharp"
}
```

Supported intensity levels:

- weak
- medium
- strong

Supported peak shapes:

- sharp
- broad
- very broad

---

## Pseudo-IR Spectrum Generation

Pipeline:

```text
SMILES
↓
SMARTS Pattern Matching
↓
Functional Groups
↓
IR Band Assignment
↓
Intensity & Shape Modeling
↓
Pseudo IR Spectrum
```

Features:

- Gaussian peak generation
- Automatic peak positioning
- Intensity-based peak depth
- Shape-based peak width
- IR-style axis orientation
- Peak annotations

---

## Example Capabilities

### Paracetamol

Detected groups:

- Aromatic Ring
- Phenol
- Amide

Predicted IR features:

- O-H stretch
- N-H stretch
- Amide C=O stretch
- Aromatic C=C stretch
- Ar-O stretch

### Ketamine

Detected groups:

- Aromatic Ring
- Amine
- Ketone

Predicted IR features:

- N-H stretch
- Ketone C=O stretch
- Aromatic ring vibrations

---

## Key Achievements

### v0.5 Molecular Descriptor Analysis

- RDKit descriptor pipeline
- Statistical analysis
- Correlation analysis
- Outlier analysis

### v0.6 Spectroscopy Foundations

- SMARTS-based functional group detection
- Functional group validation
- IR band library
- Intensity model
- Peak shape model
- Pseudo-IR spectrum generation

---

## Next Release

### v0.7 NMR Foundations

Planned topics:

- Proton environments
- Aromatic proton prediction
- CH₃ / CH₂ classification
- Functional-group-based NMR assignments
- Pseudo ¹H-NMR spectra

---

## License

Educational and research project.
