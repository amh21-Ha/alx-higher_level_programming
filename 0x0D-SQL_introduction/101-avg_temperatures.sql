mysql -h localhost -u root -p hbtn_0c_0 < tempratures.sql

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC;
