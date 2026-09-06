from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import (create_tables, insert_compound, get_compound_by_id)

create_tables()

racemic_ibuprofen = {"record_id": 3544,
           "common_name": "Ibuprofen (Racemate)",
           "cas_number": "15687-27-1",
           "smiles": "CC(C)Cc1ccc(C(C)C(=O)O)cc1",
           "formula": "C_{13}H_{18}O_{2}",
           "inchi": "InChI=1/C13H18O2/c1-9(2)8-11-4-6-12(7-5-11)10(3)13(14)15/h4-7,9-10H,8H2,1-3H3,(H,14,15)",
           "inchi_key": "HEFNNWSXXWATRW-UHFFFAOYNA-N",
           "molecular_weight": 206.285}

s_ibuprofen = {"record_id": 36498,
           "common_name": "(S)-Ibuprofen",
           "cas_number": "51146-56-6",
           "smiles": "CC(C)Cc1ccc([C@H](C)C(=O)O)cc1",
           "formula": "C_{13}H_{18}O_{2}",
           "inchi": "InChI=1/C13H18O2/c1-9(2)8-11-4-6-12(7-5-11)10(3)13(14)15/h4-7,9-10H,8H2,1-3H3,(H,14,15)/t10-/m0/s1",
           "inchi_key": "HEFNNWSXXWATRW-JTQLQIEINA-N",
           "molecular_weight": 206.285}

r_ibuprofen = {"record_id": 102822,
           "common_name": "(R)-Ibuprofen",
           "cas_number": "51146-57-7",
           "smiles": "CC(C)Cc1ccc([C@@H](C)C(=O)O)cc1",
           "formula": "C_{13}H_{18}O_{2}",
           "inchi": "InChI=1/C13H18O2/c1-9(2)8-11-4-6-12(7-5-11)10(3)13(14)15/h4-7,9-10H,8H2,1-3H3,(H,14,15)/t10-/m1/s1",
           "inchi_key": "HEFNNWSXXWATRW-SNVBAGLBNA-N",
           "molecular_weight": 206.285}

insert_compound(racemic_ibuprofen)
insert_compound(s_ibuprofen)
insert_compound(r_ibuprofen)
print("Ibuprofen inserted successfully.")