SELECT a - b AS difference FROM (
        SELECT COUNT(city) AS a, COUNT(DISTINCT city) AS b FROM station
    ) AS counts;

