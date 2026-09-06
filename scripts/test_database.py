from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import (create_tables, insert_compound, get_compound_by_id)

create_tables()

aspirin = {"record_id": 2157,
           "common_name": "Aspirin",
           "cas_number": "50-78-2",
           "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
           "formula": "C9H8O4",
           "inchi": "InChI=1S/C9H8O4/c1-6(10)13-9-5-3-2-4-7(9)8(11)12/h2-5H,1H3,(H,11,12)",
           "inchi_key": "BSYNRYMUTXBXSQ-UHFFFAOYSA-N",
           "molecular_weight": 180.16}

insert_compound(aspirin)
print("Aspirin inserted successfully.")

levetiracetam = {
    "record_id": 4447633,
    "common_name": "Levetiracetam",
    "cas_number": None,
    "smiles": "CC[C@@H](C(N)=O)N1CCCC1=O",
    "formula": "C_{8}H_{14}N_{2}O_{2}",
    "inchi": "InChI=1/C8H14N2O2/c1-2-6(8(9)12)10-5-3-4-7(10)11/h6H,2-5H2,1H3,(H2,9,12)/t6-/m0/s1",
    "inchi_key": "HPHUVLMMVZITSG-LURJTMIENA-N",
    "molecular_weight": 170.212
}

insert_compound(levetiracetam)

print("Levetiracetam inserted successfully.")

compound = get_compound_by_id(2157)
print("\nRetrieved compound from database:")
print(compound)

