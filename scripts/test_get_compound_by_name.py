from pathlib import Path
import sys
import os

from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.api.rsc_client import RSCClient

load_dotenv()
client = RSCClient(os.getenv("RSC_API_KEY"))

compound = client.get_compound_by_name("Paracetamol")
print(compound)