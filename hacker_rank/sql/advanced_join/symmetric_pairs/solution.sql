SELECT DISTINCT
    LEAST(f1.x, f1.y) AS x,
    GREATEST(f1.x, f1.y) AS y
FROM functions f1
JOIN functions f2
    ON f1.x = f2.y AND f1.y = f2.x
WHERE f1.x < f1.y
   OR (f1.x = f1.y AND 
       (SELECT COUNT(*) FROM functions f3 WHERE f3.x = f1.x AND f3.y = f1.y) > 1)
ORDER BY x, y;

