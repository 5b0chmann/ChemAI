from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import (create_tables, insert_compound, get_compound_by_id)

create_tables()

paracetamol = {"record_id": 1906,
           "common_name": "Paracetamol",
           "cas_number": "103-90-2",
           "smiles": "CC(=O)Nc1ccc(O)cc1",
           "formula": "C_{8}H_{9}NO_{2}",
           "inchi": "InChI=1/C8H9NO2/c1-6(10)9-7-2-4-8(11)5-3-7/h2-5,11H,1H3,(H,9,10)",
           "inchi_key": "RZVAJINKPMORJF-UHFFFAOYNA-N",
           "molecular_weight": 151.165}

insert_compound(paracetamol)
print("Paracetamol inserted successfully.")