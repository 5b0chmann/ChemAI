from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.data.compound_registry import compound_registry

print("ChemAI Loader Design")
print("=" * 30)

for compound_name, metadata in  compound_registry.items():
    cas_number = metadata["cas"]
    compound_class = metadata["class"]

    print(f"\nName: {compound_name}")
    print(f"CAS: {cas_number}")
    print(f"Class: {compound_class}")