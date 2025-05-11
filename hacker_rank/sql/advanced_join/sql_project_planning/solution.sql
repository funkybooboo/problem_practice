WITH ordered_tasks AS (
    SELECT 
        Start_Date,
        End_Date,
        ROW_NUMBER() OVER (ORDER BY Start_Date) AS rn
    FROM Projects
),
grouped_projects AS (
    SELECT 
        Start_Date,
        End_Date,
        DATE_SUB(Start_Date, INTERVAL rn DAY) AS grp
    FROM ordered_tasks
),
project_ranges AS (
    SELECT 
        MIN(Start_Date) AS project_start,
        MAX(End_Date) AS project_end,
        DATEDIFF(MAX(End_Date), MIN(Start_Date)) AS duration
    FROM grouped_projects
    GROUP BY grp
)
SELECT 
    project_start, 
    project_end
FROM project_ranges
ORDER BY duration, project_start;

