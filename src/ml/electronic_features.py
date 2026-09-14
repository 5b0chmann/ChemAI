from rdkit.Chem import AllChem

def calculate_gasteiger_charges(mol):
    """
    Calculate Gasteiger partial charges
    for all atoms in a molecule.
    
    Returns:
    list[float]
    """

    AllChem.ComputeGasteigerCharges(mol)

    charges = []

    for atom in mol.GetAtoms():

        charge = float(atom.GetProp("_GasteigerCharge"))

        charges.append(charge)

    return charges

def get_gasteiger_charge(atom):
    """Return Gasteiger charge for a single atom."""

    return float(atom.GetProp("_GasteigerCharge"))

def get_neighbor_charges(atom):
    """Return charges of neighbor atoms."""

    charges = []

    for neighbor in atom.GetNeighbors():

        charge = float(neighbor.GetProp("_GasteigerCharge"))

        charges.append(charge)

    return charges

def get_mean_neighbor_charge(atom):
    """Average charge of neighboring atoms."""

    charges = get_neighbor_charges(atom)

    if not charges:
        return 0.0

    return sum(charges) / len(charges)

def get_max_neighbor_charge(atom):
    """Maximum neighboring charge."""

    charges = get_neighbor_charges(atom)

    if not charges:
        return 0.0

    return max(charges)

def get_min_neighbor_charge(atom):
    """Minimum neighboring charge."""

    charges = get_neighbor_charges(atom)

    if not charges:
        return 0.0

    return min(charges)