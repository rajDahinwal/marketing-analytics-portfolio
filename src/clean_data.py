
import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# 1. PATHS
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = ROOT / "data" / "raw" / "marketing_campaigns.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "marketing_campaigns_cleaned.csv"
REPORT_FILE = ROOT / "reports" / "data_quality_report.txt"

# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(RAW_FILE)

initial_rows = len(df)

print("Starting data quality analysis...")
print(f"Initial records: {initial_rows}")

# --------------------------------------------------
# 3. STANDARDISE COLUMN NAMES
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# --------------------------------------------------
# 4. CONVERT DATA TYPES
# --------------------------------------------------

date_columns = ["start_date", "end_date"]

numeric_columns = [
    "budget",
    "spend",
    "impressions",
    "clicks",
    "ctr",
    "conversions",
    "cpa",
    "revenue",
    "roas"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# --------------------------------------------------
# 5. CHECK DUPLICATES
# --------------------------------------------------

duplicate_rows = int(df.duplicated().sum())
duplicate_ids = int(df["campaign_id"].duplicated().sum())

df = df.drop_duplicates()

# --------------------------------------------------
# 6. VALIDATE DATA
# --------------------------------------------------

issues = {}

issues["missing_values"] = int(df.isnull().sum().sum())

issues["negative_budget"] = int((df["budget"] < 0).sum())
issues["negative_spend"] = int((df["spend"] < 0).sum())
issues["negative_impressions"] = int((df["impressions"] < 0).sum())
issues["negative_clicks"] = int((df["clicks"] < 0).sum())
issues["negative_conversions"] = int((df["conversions"] < 0).sum())
issues["negative_revenue"] = int((df["revenue"] < 0).sum())

issues["clicks_exceed_impressions"] = int(
    (df["clicks"] > df["impressions"]).sum()
)

issues["conversions_exceed_clicks"] = int(
    (df["conversions"] > df["clicks"]).sum()
)

issues["spend_exceeds_budget"] = int(
    (df["spend"] > df["budget"]).sum()
)

issues["invalid_date_order"] = int(
    (df["start_date"] > df["end_date"]).sum()
)

issues["invalid_dates"] = int(
    (df[date_columns].isnull().any(axis=1)).sum()
)

# --------------------------------------------------
# 7. RECALCULATE BUSINESS METRICS
# --------------------------------------------------

# CTR is represented as a ratio, not a percentage.
df["calculated_ctr"] = np.where(
    df["impressions"] > 0,
    df["clicks"] / df["impressions"],
    np.nan
)

df["calculated_cpa"] = np.where(
    df["conversions"] > 0,
    df["spend"] / df["conversions"],
    np.nan
)

df["calculated_roas"] = np.where(
    df["spend"] > 0,
    df["revenue"] / df["spend"],
    np.nan
)

# Compare existing metrics with recalculated metrics.
issues["ctr_mismatch"] = int(
    (
        ~np.isclose(
            df["ctr"],
            df["calculated_ctr"],
            rtol=0.02,
            atol=0.0001,
            equal_nan=True
        )
    ).sum()
)

issues["cpa_mismatch"] = int(
    (
        ~np.isclose(
            df["cpa"],
            df["calculated_cpa"],
            rtol=0.02,
            atol=0.01,
            equal_nan=True
        )
    ).sum()
)

issues["roas_mismatch"] = int(
    (
        ~np.isclose(
            df["roas"],
            df["calculated_roas"],
            rtol=0.02,
            atol=0.01,
            equal_nan=True
        )
    ).sum()
)

# --------------------------------------------------
# 8. ADD USEFUL ANALYTICAL COLUMNS
# --------------------------------------------------

df["campaign_duration_days"] = (
    df["end_date"] - df["start_date"]
).dt.days + 1

df["budget_utilization"] = np.where(
    df["budget"] > 0,
    df["spend"] / df["budget"],
    np.nan
)

# --------------------------------------------------
# 9. SAVE CLEANED DATA
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

# --------------------------------------------------
# 10. GENERATE QUALITY REPORT
# --------------------------------------------------

with open(REPORT_FILE, "w", encoding="utf-8") as file:

    file.write("MARKETING CAMPAIGN DATA QUALITY REPORT\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Initial rows: {initial_rows}\n")
    file.write(f"Final rows: {len(df)}\n")
    file.write(f"Duplicate full rows removed: {duplicate_rows}\n")
    file.write(f"Duplicate campaign IDs detected: {duplicate_ids}\n\n")

    file.write("VALIDATION RESULTS\n")
    file.write("-" * 45 + "\n")

    for issue, count in issues.items():
        file.write(f"{issue}: {count}\n")

    file.write("\nOUTPUT FILE\n")
    file.write(str(OUTPUT_FILE))

print("\n========== CLEANING COMPLETE ==========")

print(f"Initial records: {initial_rows}")
print(f"Final records: {len(df)}")

print("\nValidation results:")

for issue, count in issues.items():
    print(f"{issue}: {count}")

print("\nCleaned dataset saved:")
print(OUTPUT_FILE)

print("\nQuality report saved:")
print(REPORT_FILE)
