
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_FILE = ROOT / "data" / "marketing_analytics.db"
SQL_FILE = ROOT / "sql" / "analysis.sql"

connection = sqlite3.connect(DB_FILE)

sql = SQL_FILE.read_text(encoding="utf-8")
queries = [q.strip() for q in sql.split(";") if q.strip()]

for i, query in enumerate(queries, start=1):
    print(f"\n{'=' * 60}")
    print(f"ANALYSIS {i}")
    print("=" * 60)

    cursor = connection.execute(query)
    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]
    print(" | ".join(columns))

    for row in rows:
        print(" | ".join(str(value) for value in row))

connection.close()
