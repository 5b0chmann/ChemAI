from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_compound_by_id
from src.features.descriptors import calculate_descriptors

compound = get_compound_by_id(2157)
print("Compound:")
print(compound)

smiles = compound[3]  # Assuming the compound object has a 'smiles' attribute
print("\nSMILES:")
print(smiles)

descriptors = calculate_descriptors(smiles)
print("\nDescriptors:")
for key, value in descriptors.items():
    if isinstance(value, float):
        print(f"{key}: {value:.3f}")
    else:
        print(f"{key}: {value}")