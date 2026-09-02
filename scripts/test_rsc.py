from dotenv import load_dotenv
import os
import requests


load_dotenv()
API_KEY = os.getenv("RSC_API_KEY")

headers = {
    "apikey": API_KEY,
    "Accept": "application/json",    
    "User-Agent": "ChemAI/1.0"
}

query_id  = "c9bd2b20-fe4c-4e75-9a77-f67e949029ed"
status_url = f"https://api.rsc.org/compounds/v1/filter/{query_id}/status"
# url = "https://api.rsc.org/compounds/v1/filter/name"

response = requests.get(status_url, headers=headers)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)

results_url = f"https://api.rsc.org/compounds/v1/filter/{query_id}/results"

response = requests.get(results_url, headers=headers)

print("Results Status:", response.status_code)
print(response.text)

record_id = 2157
details_url = f"https://api.rsc.org/compounds/v1/records/{record_id}/details"
params = {"fields":("SMILES, Formula, CommonName,"
                    "InChI, InChIKey, MolecularWeight")}
details_response = requests.get(details_url, headers=headers, params=params)
print("\nDetails Status:", details_response.status_code)
print("Details Response:")
print(details_response.text)

   
if API_KEY:
    print("API Key loaded successfully.")
else:
    print("API Key not found. ")

# from src.api.rsc_client import RSCClient
#client = RSCClient(API_KEY)
# result = client.search_compound("Aspirin")
# print(result)
