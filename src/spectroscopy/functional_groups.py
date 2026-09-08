"""
ChemAI v0.6 Spectroscopy Foundations
Functional group detection using RDKit SMARTS patterns.
"""

from rdkit import Chem

FUNCTIONAL_GROUPS = {"Aromatic Ring": "a1aaaaa1",
                     "Alcohol": "[CX4][OX2H]",
                     "Phenol": "c[OX2H]",
                     "Carboxylic Acid": "C(=O)[OX2H1]",
                     "Amide": "C(=O)N",
                     "Amine": "[NX3;H2,H1,H0;!$(NC=O)]",
                     "Ester": "[CX3](=[OD1])[OD2][#6]",
                     "Ketone": "[CX3](=[OX1])([#6])[#6]",
                     "Ether": "[OD2]([#6])[#6]",
                     "Aliphytic Ether": "[#6X4][O][#6X4]",}

def detect_functional_groups(smiles):
    """
    Detect functional groups from a SMILES string.
    
    Parameters
    ----------
    smiles: str
        SMILES representation of a molecule.
    
    Returns
    -------
    list[str]
        List of detected functional groups.
    """
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return []

    detected_groups = []
    for group_name, smarts in FUNCTIONAL_GROUPS.items():
        pattern = Chem.MolFromSmarts(smarts)
        if mol.HasSubstructMatch(pattern):
            detected_groups.append(group_name)

    return detected_groups
