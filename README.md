# ChemAI

ChemAI is a computational chemistry and data science project.

## Project Goal

The goal of ChemAI is to build a complete chemical data pipeline using the Royal Society of Chemistry (RSC) API as the primary data source.

Instead of relying on pre-built datasets, chemical information is collected, processed, stored, and prepared for machine learning workflows.

## Current Features

### RSC API Integration

- RSC API authentication
- Compound search by name
- Query status tracking
- Query result retrieval
- Compound detail retrieval
- External reference retrieval
- OpenAPI-based API exploration

### SQLite Persistence Layer

- Compound storage
- Compound retrieval by record ID
- CAS number storage
- SMILES storage
- Molecular metadata storage

### RDKit Feature Engineering

- SMILES to Mol object conversion
- Molecular graph analysis
- Ring structure identification
- Descriptor calculation

Currently supported descriptors:

- Molecular Weight
- logP
- TPSA
- H-Bond Donors
- H-Bond Acceptors
- Rotatable Bonds
- Ring Count
- Number of Atoms
- Number of Bonds

## Example Workflow

```text
RSC API
    ↓
Compound Search
    ↓
Record ID
    ↓
SQLite Database
    ↓
SMILES
    ↓
RDKit
    ↓
Feature Vector
```

## Example Compound

### Aspirin

Record ID:

2157

CAS Number:

50-78-2

SMILES:

```text
CC(=O)OC1=CC=CC=C1C(=O)O
```

Generated Feature Vector:

```text
Molecular Weight: 180.159
logP: 1.310
TPSA: 63.600
H-Donors: 1
H-Acceptors: 3
Rotatable Bonds: 2
Ring Count: 1
Atoms: 13
Bonds: 13
```

## Technology Stack

- Python
- Requests
- SQLite
- RDKit
- REST APIs
- OpenAPI
- Git
- GitHub
- VS Code

## Project Status

Current Version: v0.3

### Completed Milestones

#### v0.1 - RSC API Integration

- Successful RSC API connection
- Compound search workflow
- Query status workflow
- Molecular detail retrieval

#### v0.2 - SQLite Persistence Layer

- SQLite database implementation
- Compound storage
- Compound retrieval
- First stored compound: Aspirin

#### v0.3 - RDKit Feature Engineering

- SMILES processing
- Molecular graph exploration
- Descriptor calculation
- SQLite → RDKit pipeline

## Next Milestone (v0.4)

- Multiple compounds
- Dataset generation
- Pandas DataFrame creation
- Preparation for scikit-learn models

## Author

Sebastian Bochmann