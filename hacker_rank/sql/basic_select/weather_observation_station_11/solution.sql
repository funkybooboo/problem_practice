SELECT DISTINCT city
FROM station
WHERE NOT (LOWER(city) REGEXP '^[aeiou]') 
   OR NOT (LOWER(city) REGEXP '[aeiou]$');

