from  pathlib import Path
import sys
import os
import time

from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.api.rsc_client import RSCClient
from src.data.compound_registry import compound_registry
from src.data.transformers import rsc_to_compound_dict
from src.database.database import (create_tables, insert_compound, compound_exists)

create_tables()

load_dotenv()

api_key = os.getenv("RSC_API_KEY")
client = RSCClient(api_key)

print("ChemAI Compound Loader")
print("=" * 40)

print(f"\nCompounds in registry: {len(compound_registry)}")

success_count = 0
failure_count = 0
warning_count = 0

warning_compounds = []
failed_compounds = []

for compound_name, metadata in compound_registry.items():

    if compound_exists(compound_name):

        print(
            f"Skipping existing compound: "
            f"{compound_name}"
        )

        continue

    print(f"\nLoading: {compound_name}")

    try:
        compound = client.get_compound_by_name(compound_name)

        if compound["count"] > 1:
            warning_count += 1
            warning_compounds.append(compound_name)
            result_count = compound["count"]
            print(f"WARNING: {compound_name} "
                  f"returned {result_count} results.")
            continue
        compound_dict = rsc_to_compound_dict(compound, metadata)
        insert_compound(compound_dict)

        success_count += 1

        print(f"Found: {compound['commonName']}")
        print(f"Record ID: {compound['id']}")

        time.sleep(1)
    except Exception as error:

        if "429" in str(error):

            failure_count += 1

            failed_compounds.append(compound_name)

            print(
                f"Rate limit reached while loading "
                f"{compound_name}"
            )

            print("Waiting 60 seconds...")
            time.sleep(60)
            
            continue

        failure_count += 1
        failed_compounds.append(compound_name)
        print(f"Failed: {compound_name}")
        print(error)

print("\n")
print("=" * 40)
print("IMPORT SUMMARY")
print("=" * 40)

if warning_compounds:

    print("\nWarning Compounds:")
    for compound in warning_compounds:
        print(f" - {compound}")

if failed_compounds:

    print("\nFailed Compounds:")
    for compound in failed_compounds:
        print(f" - {compound}")

print(f"Successful: {success_count}")
print(f"Warnings: {warning_count}")
print(f"Failed: {failure_count}")
print(f"Registry Entries: {len(compound_registry)}")
