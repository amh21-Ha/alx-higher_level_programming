--mysql -h localhost -u root -p hbtn_0c_0 < path/to/your/table_dump.sql

USE hbtn_0c_0;

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

