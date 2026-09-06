from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.database.database import get_all_compounds

compounds = get_all_compounds()
print(f"Number of compounds: {len(compounds)}")
print(f"\nCompounds:")
     
for compound in compounds:
    print(compound)