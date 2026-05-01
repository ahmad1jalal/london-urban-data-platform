--total traffic over time
SELECT date(datetime) AS date,
SUM(total_vehicles) AS total_traffic
FROM fact_traffic
GROUP BY date
ORDER BY date;

-- Peak Hours
SELECT EXTRACT(HOUR FROM datetime) AS hour,
AVG(total_vehicles) AS avg_traffic
FROM fact_traffic
GROUP BY hour
ORDER BY avg_traffic DESC;


-- top busy road
SELECT d.road_name,
AVG(f.total_vehicles) AS avg_traffic
FROM dim_location AS d
JOIN fact_traffic AS f
ON d.location_id = f.location_id
GROUP BY d.road_name
ORDER BY avg_traffic DESC;


-- day vs night traffic trend
SELECT 
CASE 
        WHEN EXTRACT(HOUR FROM datetime) BETWEEN 7 AND 19 THEN 'Day'
        ELSE 'Night'
    END AS period,
AVG(total_vehicles) As avg_traffic
FROM fact_traffic
GROUP BY period;

--Traffic trend over time
SELECT datetime,
total_vehicles,
COALESCE(LAG(total_vehicles) OVER(ORDER BY datetime),0) AS prev_traffic,
COALESCE(total_vehicles  - LAG(total_vehicles) OVER(ORDER BY datetime),0) AS traffic_change
FROM fact_traffic;

--rolling average
SELECT datetime,
AVG(total_vehicles) OVER(ORDER BY datetime
ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM fact_traffic;

-- top 10 % traffic roads
SELECT * FROM(
SELECT *,
NTILE(10) OVER(ORDER BY total_vehicles DESC) AS bucket
FROM fact_traffic
)t
WHERE bucket = 1;







