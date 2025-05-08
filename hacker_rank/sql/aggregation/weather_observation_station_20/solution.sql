SET @rowindex := -1;

SELECT
    ROUND(AVG(lat_n), 4) AS Median
FROM (
    SELECT @rowindex := @rowindex + 1 AS rowindex, s.lat_n
    FROM station s
    ORDER BY s.lat_n
) AS ordered
WHERE ordered.rowindex IN (FLOOR(@rowindex / 2), CEIL(@rowindex / 2));

