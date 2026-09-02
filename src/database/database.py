import sqlite3
from pathlib import Path

Project_root = Path(__file__).resolve().parents[2]
DB_PATH = Project_root / "data" / "chemai.db"

def get_connection():
    """Get a connection to the SQLite database."""
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    """Create the necessary tables in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compounds (
            record_id INTEGER PRIMARY KEY,
            common_name TEXT NOT NULL,
            cas_number TEXT UNIQUE,
            smiles TEXT,
            formula TEXT,
            inchi TEXT,
            inchi_key TEXT,
            molecular_weight REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_compound(compound):
    """Insert a compound into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO compounds (record_id, common_name, cas_number, smiles, formula, inchi, inchi_key, molecular_weight)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        compound['record_id'],
        compound['common_name'],
        compound['cas_number'],
        compound['smiles'],
        compound['formula'],
        compound['inchi'],
        compound['inchi_key'],
        compound['molecular_weight']
    ))
    conn.commit()
    conn.close()

def get_compound_by_id(record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compounds WHERE record_id = ?", (record_id,))
    result = cursor.fetchone()
    conn.close()
    return result
