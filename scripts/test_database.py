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

compound = get_compound_by_id(2157)
print("\nRetrieved compound from database:")
print(compound)