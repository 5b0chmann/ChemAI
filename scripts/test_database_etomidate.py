from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import (create_tables, insert_compound, get_compound_by_id)

create_tables()

racemic_etomidate = {"record_id": 33418,
           "common_name": "rac-Etomidate",
           "cas_number": None,
           "smiles": "CCOC(=O)c1cncn1C(C)c1ccccc1",
           "formula": "C_{14}H_{16}N_{2}O_{2}",
           "inchi": "InChI=1/C14H16N2O2/c1-3-18-14(17)13-9-15-10-16(13)11(2)12-7-5-4-6-8-12/h4-11H,3H2,1-2H3",
           "inchi_key": "NPUKDXXFDDZOKR-UHFFFAOYNA-N",
           "molecular_weight": 244.294}

positive_etomidate = {"record_id": 580864,
           "common_name": "(+)-Etomidate",
           "cas_number": None,
           "smiles": "CCOC(=O)c1cncn1[C@H](C)c1ccccc1",
           "formula": "C_{14}H_{16}N_{2}O_{2}",
           "inchi": "InChI=1/C14H16N2O2/c1-3-18-14(17)13-9-15-10-16(13)11(2)12-7-5-4-6-8-12/h4-11H,3H2,1-2H3/t11-/m1/s1",
           "inchi_key": "NPUKDXXFDDZOKR-LLVKDONJNA-N",
           "molecular_weight": 244.294}

negative_etomidate = {"record_id": 4892424,
           "common_name": "(-)-Etomidate",
           "cas_number": None,
           "smiles": "CCOC(=O)c1cncn1[C@@H](C)c1ccccc1",
           "formula": "C_{14}H_{16}N_{2}O_{2}",
           "inchi": "InChI=1/C14H16N2O2/c1-3-18-14(17)13-9-15-10-16(13)11(2)12-7-5-4-6-8-12/h4-11H,3H2,1-2H3/t11-/m0/s1",
           "inchi_key": "NPUKDXXFDDZOKR-NSHDSACANA-N",
           "molecular_weight": 244.294}

insert_compound(racemic_etomidate)
insert_compound(positive_etomidate)
insert_compound(negative_etomidate)
print("Etomidate inserted successfully.")