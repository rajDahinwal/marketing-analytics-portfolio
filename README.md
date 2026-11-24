# Marketing Campaign Performance Analysis

## Project Overview

An end-to-end marketing analytics project analyzing 1,000 synthetic marketing campaign records across six channels.

The project demonstrates how Python, SQL and data visualization can be used to evaluate campaign performance and identify opportunities for improvement.

## Business Questions

- Which marketing channels generate the highest ROAS?
- Which channels have the lowest cost per conversion?
- Which campaigns exceed their allocated budgets?
- Which campaigns generate less revenue than their advertising spend?
- How does ROAS change over time?

## Tools and Technologies

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- Git

## Project Structure

```text
marketing-analytics-portfolio/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── sql/
├── visuals/
├── reports/
├── README.md
└── requirements.txt
```

## Key Findings

- Overall ROAS: 3.39
- Email had the highest channel ROAS: 5.25.
- Affiliate had the second-highest channel ROAS: 4.98.
- Video had the lowest channel ROAS: 1.92.
- 149 campaigns exceeded their individual budgets.
- 56 campaigns recorded ROAS below 1.

## Visualizations

The project includes:

1. ROAS by marketing channel
2. Monthly ROAS trend
3. Budget versus actual spend by channel

See the `visuals/` folder.

## Report

The detailed analysis and recommendations are available in:

`reports/marketing_performance_report.md`

## Data Source and Disclaimer

The dataset contains synthetic, fictional marketing campaign data. It is used for demonstration and portfolio purposes only. It does not represent actual client campaigns or business results.

Currency is not specified in the source dataset. ROAS represents revenue divided by advertising spend and should not be interpreted as profit.

## Project Objective

Demonstrate practical skills in data cleaning, SQL analysis, performance measurement and business reporting.