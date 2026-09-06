from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds
from src.features.descriptors import calculate_descriptors

compounds = get_all_compounds()

for compound in compounds:
    name = compound[1]
    smiles = compound[3]

    descriptors = calculate_descriptors(smiles)
    print(f"\n{name}")
    for key, value in descriptors.items():
        if isinstance(value, float):
            print(f"{key}: {value:.3f}")
        else:
            print(f"{key}: {value}")