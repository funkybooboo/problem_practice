SELECT * FROM (SELECT city, LENGTH(city) AS len FROM station ORDER BY LENGTH(city) DESC, city ASC LIMIT 1) AS l
UNION
SELECT * FROM (SELECT city, LENGTH(city) AS len FROM station ORDER BY LENGTH(city) ASC, city ASC LIMIT 1) AS s;

