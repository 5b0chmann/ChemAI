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

    def search_compound(self, query: str, page_size: int = 20) -> Dict:
        """Search for a compound using the RSC API."""
        return self.get("compounds/search", {"query": query, "pageSize": page_size})

    def compound_by_cas(self, cas_number: str) -> Dict:
        """Retrieve compound information by CAS number."""

        return self._get(f"compounds/cas/{cas_number}")

    def compound_by_id(self, compound_id: str) -> Dict:
        """Retrieve compound information by RSC compound ID."""
        return self._get(f"compounds/{compound_id}")

    def healthcheck(self) -> bool:
        """API connectivity check."""
        try:
            self._get("/")
            return True
        except Exception:
            return False

    


        