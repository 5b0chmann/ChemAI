from rdkit import Chem

def get_atom_features(atom):
    """
    Extract atom-level features from a RDKit atom.
    """

    return{"atomic_number": atom.GetAtomicNum(),
           "Symbol": atom.GetSymbol(),
           "degree": atom.GetDegree(),
           "formal_charge": atom.GetFormalCharge(),
           "is_aromatic": atom.GetIsAromatic(),
           "is_in_ring": atom.IsInRing(),
           "hybridization": str(atom.GetHybridization()),
           "num_hydrogens": atom.GetTotalNumHs(),
           "valence": atom.GetTotalValence(),}

def get_neighbor_summary(atom):

    neighbors = atom.GetNeighbors()

    return {"neighbor_c": sum(n.GetAtomicNum() ==6
                              for n in neighbors),
            "neighbor_n": sum(n.GetAtomicNum() ==7
                              for n in neighbors),
            "neighbor_o": sum(n.GetAtomicNum() == 8
                              for n in neighbors),
            "neighbor_halogen": sum(n.GetAtomicNum()
                                    in [9, 17, 35, 53]
                                    for n in neighbors)}

def get_atom_feature_vector(atom):

    features = get_atom_features(atom)
    neighbors = get_neighbor_summary(atom)

    return[features["atomic_number"],
           features["degree"],
           features["formal_charge"],
           features["valence"],
           int(features["is_aromatic"]),
           int(features["is_in_ring"]),
           features["num_hydrogens"],

           neighbors["neighbor_c"],
           neighbors["neighbor_n"],
           neighbors["neighbor_o"],
           neighbors["neighbor_halogen"]]