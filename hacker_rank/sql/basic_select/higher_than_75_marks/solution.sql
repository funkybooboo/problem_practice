SELECT name
FROM students
WHERE marks > 75
ORDER BY 
    SUBSTRING(name FROM LENGTH(name) - 2 FOR 3),
    id;

