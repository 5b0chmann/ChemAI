from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.features.descriptors import calculate_descriptors

smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
descriptors = calculate_descriptors(smiles)
print(descriptors)