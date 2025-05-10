SELECT 
    s.name
FROM students s
JOIN friends f 
    ON s.id = f.id
JOIN packages sp 
    ON s.id = sp.id
JOIN packages fp 
    ON f.friend_id = fp.id
WHERE fp.salary > sp.salary
ORDER BY fp.salary;

