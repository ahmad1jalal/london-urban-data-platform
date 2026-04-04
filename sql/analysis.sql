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
