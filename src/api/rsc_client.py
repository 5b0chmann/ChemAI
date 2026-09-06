"""Royal Society of Chemistry API Client for ChemAI."""

from __future__ import annotations
import requests
from typing import Dict, Optional

class RSCClient:
    """Client for interacting with the Royal Society of Chemistry API."""
    BASE_URL = "https://api.rsc.org/compounds/v1/"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"apikey": api_key, "Accept": "application/json", "user-agent": "ChemAI/1.0"})

    def get(self, endpoint: str, params: Optional[dict] = None) -> Dict:
        """Make a GET request to the RSC API."""
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def create_name_query(self, compound_name: str) -> Dict:
        """Create a name search query."""
        url = f"{self.BASE_URL}filter/name"
        payload = {"name": compound_name}
        response=self.session.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()

    def get_query_status(self, query_id: str) -> Dict:
        """Get query status"""
        endpoint = f"filter/{query_id}/status"
        return self.get(endpoint)

    def get_query_results(self, query_id: str) -> Dict:
        """Get query results"""
        endpoint = f"filter/{query_id}/results"
        return self.get(endpoint)

    def get_compound_details(self, record_id: int) -> Dict:
        """Get compound details"""
        endpoint = f"records/{record_id}/details"
        params = {"fields":("SMILES, Formula, CommonName,"
                    "InChI, InChIKey, MolecularWeight")}
        return self.get(endpoint, params=params)

    def get_compound_by_name(self, compound_name: str) -> Dict:
        """Retrieve compound details by compound name."""
        query = self.create_name_query(compound_name)
        query_id = query["queryId"]

        status = self.get_query_status(query_id)
        if status["status"] != "Complete":
            raise RuntimeError(f"Query not complete: {status}")

        results = self.get_query_results(query_id)
        count = len(results["results"])
        if count == 0:
            raise ValueError(f"No results found for {compound_name}")
        
        record_id = results["results"][0]
        details = self.get_compound_details(record_id)
        details["count"] = count
        return details
        

    def search_compound(self, query: str, page_size: int = 20) -> Dict:
        """Search for a compound using the RSC API."""
        return self.get("compounds/search", {"query": query, "pageSize": page_size})


#    def compound_by_cas(self, cas_number: str) -> Dict:
#        """Retrieve compound information by CAS number."""
#
#        return self._get(f"compounds/cas/{cas_number}")

#    def compound_by_id(self, compound_id: str) -> Dict:
#        """Retrieve compound information by RSC compound ID."""
#        return self._get(f"compounds/{compound_id}")

# TODO:
# Verify whether RSC supports CAS lookup.
# Future ChemAI versions should support searching by CAS number.

#    def healthcheck(self) -> bool:
#        """API connectivity check."""
#        try:
#            self._get("")
#            return True
#        except Exception:
#            return False

    


        