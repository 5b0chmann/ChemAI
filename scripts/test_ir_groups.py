from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.spectroscopy.functional_groups import detect_functional_groups
from src.spectroscopy.ir_groups import get_ir_bands

compounds = get_all_compounds()

for compound in compounds:

    name = compound[1]
    smiles = compound[3]

    groups = detect_functional_groups(smiles)
    bands = get_ir_bands(groups)

    print(f"\n{name}")
    print("-" * 40)

    print("Groups:")
    for group in groups:
        print(f"   -{group}")

    print("\nExpected IR bands:")
    
    for band in bands:
        print(f"   -{band['band']} | "
              f"{band['range']} | "
              f"{band['intensity']} | "
              f"{band['shape']}")
