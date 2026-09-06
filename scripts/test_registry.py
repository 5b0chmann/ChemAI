from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.data.compound_registry import compound_registry

print(f"Number of compounds: {len(compound_registry)}")
for compound_name, metadata in compound_registry.items():

    print()
    print("Compound:", compound_name)
    print("CAS:", metadata["cas"])
    print("Class:", metadata["class"])