from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import (create_tables, insert_compound, get_compound_by_id)

create_tables()

racemic_naproxen = {"record_id": 1262,
           "common_name": "Naproxen (Racemate)",
           "cas_number": None,
           "smiles": "COc1ccc2cc(C(C)C(=O)O)ccc2c1",
           "formula": "C_{14}H_{14}O_{3}",
           "inchi": "InChI=1/C14H14O3/c1-9(14(15)16)10-3-4-12-8-13(17-2)6-5-11(12)7-10/h3-9H,1-2H3,(H,15,16)",
           "inchi_key": "CMWTZPSULFXXJA-UHFFFAOYNA-N",
           "molecular_weight": 230.263}

s_naproxen = {"record_id": 137720,
           "common_name": "(S)-Naproxen",
           "cas_number": None,
           "smiles": "COc1ccc2cc([C@H](C)C(=O)O)ccc2c1",
           "formula": "C_{14}H_{14}O_{3}",
           "inchi": "InChI=1/C14H14O3/c1-9(14(15)16)10-3-4-12-8-13(17-2)6-5-11(12)7-10/h3-9H,1-2H3,(H,15,16)/t9-/m0/s1",
           "inchi_key": "CMWTZPSULFXXJA-VIFPVBQENA-N",
           "molecular_weight": 230.263}

insert_compound(racemic_naproxen)
insert_compound(s_naproxen)
print("Naproxen inserted successfully.")