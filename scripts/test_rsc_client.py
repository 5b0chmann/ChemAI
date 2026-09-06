from pathlib import Path
import sys
import os

from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.api.rsc_client import RSCClient

load_dotenv()
api_key = os.getenv("RSC_API_KEY")
client = RSCClient(api_key)

query = client.create_name_query("Paracetamol")
print("Query:")
print(query)

query_id = query["queryId"]
status = client.get_query_status(query_id)
print("\nStatus:")
print(status)

results = client.get_query_results(query_id)
print("\nResults:")
print(results)

record_id = results["results"][0]
details = client.get_compound_details(record_id)
print("\nDetails:")
print(details)
