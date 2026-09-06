from  pathlib import Path
import sys
import os

from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.api.rsc_client import RSCClient
from src.data.compound_registry import compound_registry
from src.data.transformers import rsc_to_compound_dict
from src.database.database import (create_tables, insert_compound)
create_tables()

load_dotenv()

api_key = os.getenv("RSC_API_KEY")
client = RSCClient(api_key)

print("ChemAI Compound Loader")
print("=" * 40)

for compound_name, metadata in compound_registry.items():
    print(f"\nLoading: {compound_name}")

    try:
        compound = client.get_compound_by_name(compound_name)
        if compound["count"] > 1:
            result_count = compound["count"]
            print(f"WARNING: {compound_name} "
                  f"returned {result_count} results.")
            continue
        compound_dict = rsc_to_compound_dict(compound, metadata)
        insert_compound(compound_dict)
        print(f"Found: {compound["commonName"]}")
        print(f"Record ID: {compound["id"]}")
    except Exception as error:
        print(f"Failed: {compound_name}")
        print(error)

