
-- 1. Overall campaign performance
SELECT
    COUNT(*) AS total_campaigns,
    ROUND(SUM(budget), 2) AS total_budget,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue) / NULLIF(SUM(spend), 0), 2) AS overall_roas
FROM marketing_campaigns;


-- 2. Performance by marketing channel
SELECT
    channel,
    COUNT(*) AS campaign_count,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue) / NULLIF(SUM(spend), 0), 2) AS roas,
    ROUND(SUM(spend) / NULLIF(SUM(conversions), 0), 2) AS cost_per_conversion
FROM marketing_campaigns
GROUP BY channel
ORDER BY roas DESC;


-- 3. Top 10 campaigns by revenue
SELECT
    campaign_id,
    campaign_name,
    channel,
    spend,
    revenue,
    conversions,
    roas
FROM marketing_campaigns
ORDER BY revenue DESC
LIMIT 10;


-- 4. Campaigns spending more than their budget
SELECT
    campaign_id,
    campaign_name,
    channel,
    budget,
    spend,
    ROUND(spend - budget, 2) AS overspend_amount,
    ROUND((spend - budget) / NULLIF(budget, 0) * 100, 2) AS overspend_percentage
FROM marketing_campaigns
WHERE spend > budget
ORDER BY overspend_amount DESC;


-- 5. Campaigns with ROAS below 1
SELECT
    campaign_id,
    campaign_name,
    channel,
    spend,
    revenue,
    roas
FROM marketing_campaigns
WHERE roas < 1
ORDER BY roas ASC;


-- 6. Monthly performance
SELECT
    strftime('%Y-%m', start_date) AS campaign_month,
    COUNT(*) AS campaign_count,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue) / NULLIF(SUM(spend), 0), 2) AS roas
FROM marketing_campaigns
GROUP BY campaign_month
ORDER BY campaign_month;
