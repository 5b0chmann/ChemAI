from rdkit import Chem
from rdkit.Chem import Descriptors

smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
mol = Chem.MolFromSmiles(smiles)

print("SMILES:", smiles)
print("Mol:", mol)
print("Type:", type(mol))

print("\nAtoms:", mol.GetNumAtoms())
print("Bonds:", mol.GetNumBonds())

print("\nAtom Details:")
for atom in mol.GetAtoms():
    print(f"Index: {atom.GetIdx():2d}",
          f"Symbol: {atom.GetSymbol():2s}",
          f"Atomic Number: {atom.GetAtomicNum()}")

print("\nBond Detail:")
for bond in mol.GetBonds():
    print(f"From: {bond.GetBeginAtomIdx():2d}",
          f"To: {bond.GetEndAtomIdx():2d}",
          f"Type: {bond.GetBondType()}")

ring_info = mol.GetRingInfo()
print()
print("Ring Count:", ring_info.NumRings())

for atom in mol.GetAtoms():
    print(atom.GetSymbol(),
          "Degree:", atom.GetDegree())

print("\nAtom Neighbors:")
for atom in mol.GetAtoms():
    neighbors = [neighbor.GetSymbol() for neighbor in atom.GetNeighbors()]
    print(f"{atom.GetIdx():2d}", atom.GetSymbol(), "->", neighbors)

print("\nBond Types:")
for bond in mol.GetBonds():
    print(f"{bond.GetBeginAtomIdx():2d} ->"
          f"{bond.GetEndAtomIdx():2d}",
           f"Type: {bond.GetBondType()}")

print("\nRing Atoms:")
for ring in ring_info.AtomRings():
    print("\nRing:")
    for atom_idx in sorted(ring):
        atom = mol.GetAtomWithIdx(atom_idx)
        print(f"Atom {atom_idx}:", atom.GetSymbol())

print()
print("Molecular Weight:", round(Descriptors.MolWt(mol), 3))
print("logP:", round(Descriptors.MolLogP(mol), 3))
print("TPSA:", round(Descriptors.TPSA(mol), 3))
print("H-Donors:", Descriptors.NumHDonors(mol))
print("H-Acceptors:", Descriptors.NumHAcceptors(mol))