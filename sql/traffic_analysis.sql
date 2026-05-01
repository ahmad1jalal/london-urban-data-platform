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