from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("RSC_API_KEY")

headers ={"apikey": API_KEY,
          "Accept": "application/json",
          "User-Agent": "ChemAI/1.0"}

url = "https://api.rsc.org/compounds/v1/filter/name"

payload = {"name": "Ibuprofen"}

response = requests.post(url, headers= headers, json=payload)

print("Status:", response.status_code)
print("Response:")
print(response.text)

query_id = "0099ef54-a2b7-4863-9ec9-ed7ef3faa5b0"
status_url =(f"https://api.rsc.org/compounds/v1/filter/{query_id}/status")

response = requests.get(status_url, headers=headers)
print("\nStatus Check:")
print(response.status_code)
print(response.text)

results_url = (f"https://api.rsc.org/compounds/v1/filter/{query_id}/results")
response = requests.get(results_url, headers=headers)

print("\nResults:")
print("Status:", response.status_code)
print(response.text)

record_id = 102822
details_url = f"https://api.rsc.org/compounds/v1/records/{record_id}/details"
params = {"fields":("SMILES, Formula, CommonName,"
                    "InChI, InChIKey, MolecularWeight")}
details_response = requests.get(details_url, headers=headers, params=params)
print("\nDetails Status:", details_response.status_code)
print("Details Response:")
print(details_response.text)