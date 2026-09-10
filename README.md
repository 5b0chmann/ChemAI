# ChemAI

## Current Version
**v0.7.1 Machine Learning Foundations**

## Overview
ChemAI is a cheminformatics and machine learning project focused on understanding molecular structure, electronic environments, and spectroscopy.

## Completed Milestones

### v0.1 - RSC API Integration
- Retrieval of compound data from the Royal Society of Chemistry

### v0.2 - Database Foundations
- SQLite compound database

### v0.3 - RDKit Feature Engineering
- Molecular descriptors
- Structural analysis

### v0.4 - Dataset Builder
- Curated pharmaceutical dataset

### v0.5 - Molecular Descriptor Analysis
- Descriptor statistics
- Correlation analysis

### v0.6 - Spectroscopy Foundations
- SMARTS-based functional group detection
- IR band library
- Intensity and peak shape modelling
- Pseudo IR spectrum generation

### v0.7.1 - Machine Learning Foundations
- Atom-level electronic environment features
- Ring-size detection
- Bond-type features
- Aromatic neighbor features
- Atom feature matrix generation
- PCA analysis of atomic environments

## Atom Feature Vector
Features currently include:
- atomic_number
- degree
- formal_charge
- valence
- hybridization
- is_aromatic
- is_in_ring
- ring_size
- num_hydrogens
- neighbor_c
- neighbor_n
- neighbor_o
- neighbor_halogen
- aromatic_neighbors
- single_bonds
- double_bonds
- triple_bonds

## Dataset Statistics
- 20 pharmaceutical compounds
- 312 atom environments
- 20 feature columns

## Vision
Structure -> Electronic Environment -> Machine Learning -> Spectral Prediction

Future goals include Gasteiger charges, NMR prediction, IR frequency prediction and graph neural networks.
