from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.spectroscopy.functional_groups import (detect_functional_groups)
from src.spectroscopy.ir_groups import(get_ir_bands)
from src.spectroscopy.ir_plot import (generate_ir_spectrum, plot_ir_spectrum)

smiles = "CC(=O)Nc1ccc(O)cc1"  # Paracetamol

groups = detect_functional_groups(smiles)

bands = get_ir_bands(groups)

x, spectrum, labels = generate_ir_spectrum(bands)

plot_ir_spectrum(x, spectrum, labels, "Paracetamol Pseudo IR Spectrum")