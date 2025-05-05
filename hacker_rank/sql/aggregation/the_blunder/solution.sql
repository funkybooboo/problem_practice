SELECT CEIL(ABS(
    AVG(salary) - 
    AVG(CAST(REPLACE(salary, '0', '') AS UNSIGNED))
)) AS error
FROM EMPLOYEES;

