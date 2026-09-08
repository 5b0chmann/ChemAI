"""
ChemAI v0.6 Spectroscopy Foundations
IR-relevant functional group assignments.
"""
IR_GROUPS = {"Alcohol": ["O-H stretch: 3200-3600 cm-1"],
             "Phenol": ["O-H stretch: 3200-3600 cm-1",
                        "Ar-O stretch: 1200-1260 cm-1"],
            "Carboxylic Acid": ["O-H stretch: 2500-3300 cm-1",
                                "C=O stretch: 1700-1725 cm-1"],
            "Ester": ["C=O stretch: 1735-1750 cm-1",
                      "C-O stretch: 1050-1300 cm-1"],
            "Ketone": ["C=O stretch: 1705-1725 cm-1"],
            "Amide": ["N-H stretch: 3200-3500 cm-1",
                      "Amide C=O stretch: 1630-1690 cm-1"],
            "Amine": ["N-H stretch: 3300-3500 cm-1"],
            "Ether": ["C-O stretch: 1000-1300 cm-1"],
            "Aromatic Ring": ["Aromatic C=C stretch: 1450-1600 cm-1",
                              "Aromatic C-H stretch: 3000-3100 cm-1"]}

IR_GROUPS = {"Alcohol": [{"band": "O-H stretch", "range": "3200-3600 cm-1", "intensity":"strong", "shape": "broad"}],
             "Phenol": [{"band": "O-H stretch", "range": "3200-3600 cm-1", "intensity":"strong", "shape": "broad"},
                        {"band": "Ar-O stretch", "range": "1200-1260 cm-1", "intensity": "medium", "shape": "sharp"}],
            "Carboxylic Acid": [{"band":"O-H stretch", "range": "2500-3300 cm-1", "intensity": "strong", "shape": "very broad"},
                                {"band": "C=O stretch", "range": "1700-1725 cm-1", "intensity": "strong", "shape": "sharp"}],
            "Ester": [{"band": "C=O stretch", "range": "1735-1750 cm-1", "intensity": "strong", "shape": "sharp"},
                      {"band": "C-O stretch", "range": "1050-1300 cm-1", "intensity": "strong", "shape": "sharp"}],
            "Ketone": [{"band": "C=O stretch", "range": "1705-1725 cm-1", "intensity": "strong", "shape": "sharp"}],
            "Amide": [{"band": "N-H stretch", "range": "3200-3500 cm-1", "intensity": "medium", "shape": "broad"},
                      {"band":"Amide C=O stretch", "range": "1630-1690 cm-1", "intensity":"strong", "shape": "sharp"}],
            "Amine": [{"band": "N-H stretch", "range": "3300-3500 cm-1", "intensity": "medium", "shape": "broad"}],
            "Ether": [{"band": "C-O stretch", "range": "1000-1300 cm-1", "intensity": "strong", "shape": "sharp"}],
            "Aromatic Ring": [{"band": "Aromatic C=C stretch", "range": "1450-1600 cm-1", "intensity": "medium", "shape": "sharp"},
                              {"band": "Aromatic C-H stretch", "range": "3000-3100 cm-1", "intensity": "weak", "shape": "sharp"}]}

def get_ir_bands(functional_groups):
    """
    Return expected IR bands for detected functional groups.
    """
    bands = []
    for group in functional_groups:
        if group in IR_GROUPS:
            bands.extend(IR_GROUPS[group])
    return bands