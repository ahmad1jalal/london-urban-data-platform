-- Top polluted sites
SELECT site,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY site
ORDER BY avg_pollution DESC;

-- Pollution tred over time..
SELECT EXTRACT(MONTH FROM readingdatetime) AS MONTH,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY EXTRACT(MONTH FROM readingdatetime)
ORDER BY avg_pollution DESC;

-- Pollution by species...
SELECT species,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY species
ORDER BY avg_pollution DESC;


-- Worst Month (highest pollution)
SELECT EXTRACT(MONTH FROM readingdatetime) AS MONTH,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY EXTRACT(MONTH FROM readingdatetime)
ORDER BY avg_pollution DESC
LIMIT 1;


-- Peak Hours
SELECT EXTRACT(HOUR FROM readingdatetime) AS Hourly,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY EXTRACT(HOUR FROM readingdatetime)
ORDER BY avg_pollution DESC;

-- Peak Week
SELECT EXTRACT(WEEK FROM readingdatetime) AS Weekly,
AVG(value) AS avg_pollution
FROM air_quality
GROUP BY EXTRACT(WEEK FROM readingdatetime)
ORDER BY avg_pollution DESC
LIMIT 5;


-- most polluted locations
SELECT dl.location_name,
AVG(faq.value) AS avg_pollution
FROM fact_air_quality AS faq
JOIN dim_location AS dl
ON faq.location_id = dl.location_id
GROUP BY dl.location_name
ORDER BY avg_pollution DESC
LIMIT 10;

-- busiest traffic locations
SELECT dl.location_name,
AVG(ft.total_vehicles) AS avg_traffic
FROM fact_traffic AS ft
JOIN dim_location AS dl
ON ft.location_id = dl.location_id
GROUP BY dl.location_name
ORDER BY avg_traffic DESC
LIMIT 5;

--pollution over time
SELECT DATE(datetime) AS day,
AVG(value) AS avg_pollution
FROM fact_air_quality
GROUP BY day;

--peak pollution hours
SELECT EXTRACT(HOUR FROM datetime) AS hour,
AVG(value) AS avg_hourly_pollution
FROM fact_air_quality
GROUP BY hour
ORDER BY avg_hourly_pollution DESC;


-- traffic impact on pollution
SELECT dl.location_name,
AVG(faq.value) AS pollution,
AVG(ft.total_vehicles) AS traffic
FROM dim_location AS dl
LEFT JOIN fact_air_quality AS faq
ON dl.location_id = faq.location_id
LEFT JOIN fact_traffic AS ft
ON ft.location_id  = dl.location_id
GROUP BY dl.location_name;