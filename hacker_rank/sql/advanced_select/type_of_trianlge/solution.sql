SELECT
    CASE
        WHEN NOT (a + b > c AND b + c > a AND c + a > b) THEN 'Not A Triangle'
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b OR b = c OR a = c THEN 'Isosceles'
        WHEN a != b AND b != c AND a != c THEN 'Scalene'
        ELSE 'Unknown'
    END AS triangle_type
FROM triangles;

