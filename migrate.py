import sqlite3
from pathlib import Path

DB = Path("/data/sqlite.db")
SCHEMA = Path("/db/schema.sql")

def migrate():
    conn = sqlite3.connect(str(DB))
    with open(SCHEMA, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate()

