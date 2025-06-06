WITH RECURSIVE nums AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1
    FROM nums
   WHERE n < 20
)
SELECT TRIM(TRAILING ' ' FROM REPEAT('* ', n)) AS pattern
FROM nums;

