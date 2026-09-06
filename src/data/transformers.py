def rsc_to_compound_dict(details, metadata):
    """Convert RSC API response to ChemAI compound format."""

    return{"record_id": details["id"],
           "common_name": details["commonName"],
           "cas_number": metadata["cas"],
           "smiles": details["smiles"],
           "formula": details["formula"],
           "inchi": details["inchi"],
           "inchi_key": details["inchiKey"],
           "molecular_weight": details["molecularWeight"]}