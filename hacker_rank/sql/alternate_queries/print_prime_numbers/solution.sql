-- change this to your desired upper bound
SET @N := 1000;

WITH RECURSIVE
  seq AS (
    SELECT 2 AS num
    UNION ALL
    SELECT num + 1
      FROM seq
     WHERE num + 1 <= @N
  ),
  primes AS (
    SELECT s.num
      FROM seq AS s
     WHERE NOT EXISTS (
       -- if any smaller number divides s.num, it's composite
       SELECT 1
         FROM seq AS d
        WHERE d.num < s.num
          AND s.num % d.num = 0
     )
  )
SELECT GROUP_CONCAT(num ORDER BY num SEPARATOR '&') AS prime_list
  FROM primes;

