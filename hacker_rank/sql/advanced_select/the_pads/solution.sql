SELECT CONCAT(name, '(', SUBSTRING(occupation, 1, 1), ')') AS combined FROM occupations ORDER BY name ASC;

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(occupation), 's.') FROM occupations GROUP BY occupation ORDER BY COUNT(*);

