
import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = ROOT / "data" / "processed" / "marketing_campaigns_cleaned.csv"
DB_FILE = ROOT / "data" / "marketing_analytics.db"

df = pd.read_csv(CSV_FILE)

connection = sqlite3.connect(DB_FILE)

df.to_sql(
    "marketing_campaigns",
    connection,
    if_exists="replace",
    index=False
)

count = connection.execute(
    "SELECT COUNT(*) FROM marketing_campaigns"
).fetchone()[0]

connection.close()

print("DATABASE CREATED SUCCESSFULLY")
print(f"Records imported: {count}")
print(f"Database location: {DB_FILE}")
