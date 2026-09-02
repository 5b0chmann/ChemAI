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
record_id = 2157
references_url = (f"https://api.rsc.org/compounds/v1/records/{record_id}/externalreferences")
response = requests.get(references_url, headers=headers)
print("Status:", response.status_code)
print("Response:")
print(response.text)