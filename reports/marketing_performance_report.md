# Marketing Campaign Performance Analysis

## 1. Project Overview

This project analyzes 1,000 fictional marketing campaign records across six marketing channels using Python, Pandas, SQLite and SQL.

**Objective:** Evaluate campaign performance, compare marketing channels, identify budget overruns and highlight underperforming campaigns.

**Data note:** The dataset is synthetic and does not represent actual client results.

## 2. Overall Performance

| Metric | Result |
|---|---:|
| Total campaigns | 1,000 |
| Total budget | 10,684,904.00 |
| Total ad spend | 9,378,483.38 |
| Total revenue | 31,757,419.07 |
| Total clicks | 13,884,811 |
| Total conversions | 299,602 |
| Overall ROAS | 3.39 |

Overall ROAS was 3.39, meaning the dataset records 3.39 units of revenue for every unit of advertising spend.

## 3. Channel Performance

| Channel | ROAS | Cost per Conversion |
|---|---:|---:|
| Email | 5.25 | 20.28 |
| Affiliate | 4.98 | 21.37 |
| Paid Search | 3.66 | 28.74 |
| Social | 2.85 | 37.50 |
| Display | 1.97 | 52.09 |
| Video | 1.92 | 55.67 |

Email and Affiliate recorded the strongest aggregate ROAS. Video and Display recorded the weakest.

## 4. Budget Analysis

- 149 campaigns spent more than their individual budgets.
- Total spending across all campaigns remained below the combined budget.
- The aggregate difference between total budget and spend was 1,306,420.62.

Individual budget overruns should be investigated rather than automatically treated as errors.

## 5. Underperforming Campaigns

A total of 56 campaigns recorded ROAS below 1.

For these campaigns, recorded revenue was lower than recorded advertising spend. These campaigns warrant further investigation.

## 6. Recommendations

1. Investigate why Email and Affiliate campaigns recorded stronger ROAS.
2. Review Video and Display campaigns for targeting, creative and conversion issues.
3. Investigate the 149 campaigns that exceeded their individual budgets.
4. Review the 56 campaigns with ROAS below 1.
5. Monitor campaign performance regularly using consistent reporting.

## 7. Tools Used

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- Visual campaign performance analysis

## 8. Limitations

- The dataset is synthetic.
- Currency is not specified in the dataset.
- ROAS measures revenue relative to advertising spend; it does not measure profit.
- The analysis identifies patterns but does not establish why a campaign performed as it did.

## 9. Conclusion

The analysis identified substantial differences in performance across marketing channels, along with individual campaign budget overruns and campaigns with ROAS below 1.

The project demonstrates a workflow for cleaning campaign data, querying a database, calculating performance metrics and presenting findings through charts and written analysis.