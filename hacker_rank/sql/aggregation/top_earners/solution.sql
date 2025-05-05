SELECT 
    MAX(total_earnings) AS max_earnings,
    COUNT(*) AS num_employees
FROM (
    SELECT 
        months * salary AS total_earnings
    FROM Employee
) AS earnings
WHERE total_earnings = (
    SELECT MAX(months * salary) FROM Employee
);

