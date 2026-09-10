from rdkit import Chem
from rdkit.Chem.rdchem import HybridizationType
from rdkit.Chem.rdchem import BondType

HYBRIDIZATION_MAP = {HybridizationType.SP: 1,
                     HybridizationType.SP2: 2,
                     HybridizationType.SP3: 3,
                     HybridizationType.SP3D: 4,
                     HybridizationType.SP3D2: 5,}

def get_atom_features(atom):
    """
    Extract atom-level features from a RDKit atom.
    """
    ring_size = 0

    for size in range(3, 9):
        if atom.IsInRingSize(size):
            ring_size = size
            break

    return{"atomic_number": atom.GetAtomicNum(),
           "symbol": atom.GetSymbol(),
           "degree": atom.GetDegree(),
           "formal_charge": atom.GetFormalCharge(),
           "is_aromatic": atom.GetIsAromatic(),
           "is_in_ring": atom.IsInRing(),
           "ring_size": ring_size,
           "hybridization": str(atom.GetHybridization()),
           "num_hydrogens": atom.GetTotalNumHs(),
           "valence": atom.GetTotalValence(),
           "hybridization_numeric": HYBRIDIZATION_MAP.get(atom.GetHybridization(),0),}

def get_neighbor_summary(atom):

    neighbors = atom.GetNeighbors()

    return {"neighbor_c": sum(n.GetAtomicNum() ==6
                              for n in neighbors),
            "neighbor_n": sum(n.GetAtomicNum() ==7
                              for n in neighbors),
            "neighbor_o": sum(n.GetAtomicNum() == 8
                              for n in neighbors),
            "neighbor_halogen": sum(n.GetAtomicNum()
                                    in (9, 17, 35, 53)
                                    for n in neighbors),
            "aromatic_neighbors": sum(n.GetIsAromatic()
                                      for n in neighbors)}

def get_bond_type_summary(atom):

    single_bonds = 0
    double_bonds = 0
    triple_bonds = 0

    for bond in atom.GetBonds():

        bond_type = bond.GetBondType()

        if bond_type == BondType.SINGLE:
            single_bonds += 1

        elif bond_type == BondType.DOUBLE:
            double_bonds += 1

        elif bond_type == BondType.TRIPLE:
            triple_bonds += 1

    return{"single_bonds": single_bonds,
           "double_bonds": double_bonds,
           "triple_bonds": triple_bonds}

def get_atom_feature_vector(atom):

    features = get_atom_features(atom)
    neighbors = get_neighbor_summary(atom)

    bonds = get_bond_type_summary(atom)

    return[features["atomic_number"],
           features["degree"],
           features["formal_charge"],
           features["valence"],
           features["hybridization_numeric"],
           int(features["is_aromatic"]),
           int(features["is_in_ring"]),
           features["ring_size"],
           features["num_hydrogens"],

           neighbors["neighbor_c"],
           neighbors["neighbor_n"],
           neighbors["neighbor_o"],
           neighbors["neighbor_halogen"],
           neighbors["aromatic_neighbors"],

           bonds["single_bonds"],
           bonds["double_bonds"],
           bonds["triple_bonds"]]

