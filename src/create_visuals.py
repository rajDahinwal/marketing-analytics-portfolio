
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_FILE = ROOT / "data" / "marketing_analytics.db"
VISUALS = ROOT / "visuals"
VISUALS.mkdir(exist_ok=True)

connection = sqlite3.connect(DB_FILE)

# Chart 1: ROAS by channel
channel = pd.read_sql_query("""
    SELECT channel,
           ROUND(SUM(revenue) / SUM(spend), 2) AS roas
    FROM marketing_campaigns
    GROUP BY channel
    ORDER BY roas DESC
""", connection)

plt.figure(figsize=(10, 6))
plt.bar(channel["channel"], channel["roas"])
plt.title("Marketing ROAS by Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig(VISUALS / "channel_roas.png", dpi=300)
plt.close()

# Chart 2: Monthly ROAS trend
monthly = pd.read_sql_query("""
    SELECT strftime('%Y-%m', start_date) AS month,
           SUM(revenue) / SUM(spend) AS roas
    FROM marketing_campaigns
    GROUP BY month
    ORDER BY month
""", connection)

plt.figure(figsize=(12, 6))
plt.plot(monthly["month"], monthly["roas"], marker="o")
plt.title("Monthly Marketing ROAS Trend")
plt.xlabel("Month")
plt.ylabel("ROAS")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(VISUALS / "monthly_roas.png", dpi=300)
plt.close()

# Chart 3: Budget versus actual spend by channel
budget = pd.read_sql_query("""
    SELECT channel,
           SUM(budget) AS budget,
           SUM(spend) AS spend
    FROM marketing_campaigns
    GROUP BY channel
    ORDER BY channel
""", connection)

budget.plot(
    x="channel",
    y=["budget", "spend"],
    kind="bar",
    figsize=(10, 6)
)
plt.title("Budget vs Actual Spend by Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Amount")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(VISUALS / "budget_vs_spend.png", dpi=300)
plt.close()

connection.close()

print("VISUALIZATION GENERATION COMPLETE")
print("Charts saved in:", VISUALS)
