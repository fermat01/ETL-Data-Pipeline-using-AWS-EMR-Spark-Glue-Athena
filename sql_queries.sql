


--- Query 1
SELECT * FROM "sales-db"."cleaned-raw" limit 5;



--- Query 2
SELECT 
    region, 
    segment, 
    SUM(forecasted_monthly_revenue) as forcast_monthly_revenue 
FROM "sales-db"."cleaned-raw" 
GROUP BY segment, region;

