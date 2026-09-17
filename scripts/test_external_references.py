from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("RSC_API_KEY")

headers = {
    "apikey": API_KEY,
    "Accept": "application/json",
    "User-Agent": "ChemAI/1.0"
}

record_id = 102822

url = (
    f"https://api.rsc.org/compounds/v1/"
    f"records/{record_id}/externalreferences")

response = requests.get(
    url,
    headers=headers
)

print("Status:")
print(response.status_code)

print("\nResponse:")

data = response.json()

print(
    json.dumps(
        data,
        indent=2
    )
)

print("\nPotential References:\n")

for reference in data.get(
    "externalReferences",
    []):

    print(
        f"{reference.get('source')} -> "
        f"{reference.get('externalId')}"
    )

    source = reference.get("source", "")
    external_id = reference.get("externalId", ""
)

    if "cas" in source.lower():
        print(
            f"Source: {source}"
        )
        print(
            f"External ID: {external_id}"
        )
