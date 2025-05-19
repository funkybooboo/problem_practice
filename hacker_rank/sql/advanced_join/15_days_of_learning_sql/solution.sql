-- Main query: for each submission date, get count of hackers with consecutive submissions,
-- and the hacker with the most submissions (and their name) on that date
SELECT
    t1.submission_date,           -- the date of submissions
    t1.unique_submissions,        -- number of hackers who have submitted every day since 2016-03-01
    t2.hacker_id,                 -- id of the hacker with most submissions on that date
    t3.name                       -- name of that hacker
FROM
    (
        -- Subquery t1: count distinct hackers with continuous submissions
        SELECT
            submission_date,
            COUNT(DISTINCT hacker_id) unique_submissions
        FROM
            submissions s
        WHERE
            (
                -- number of distinct submission dates before this date for each hacker
                SELECT COUNT(DISTINCT submission_date)
                FROM submissions
                WHERE hacker_id = s.hacker_id
                  AND submission_date < s.submission_date
            ) = DATEDIFF(s.submission_date, '2016-03-01')
        GROUP BY
            submission_date
    ) t1
JOIN
    (
        -- Subquery t2: find top hacker per date by submission count
        SELECT
            submission_date,
            (
                SELECT hacker_id
                FROM submissions
                WHERE submission_date = s.submission_date
                GROUP BY hacker_id
                ORDER BY COUNT(submission_id) DESC, hacker_id
                LIMIT 1
            ) hacker_id
        FROM
            (
                -- distinct list of submission dates
                SELECT DISTINCT submission_date
                FROM submissions
            ) s
    ) t2
    ON t1.submission_date = t2.submission_date
JOIN
    hackers t3  -- join with hackers table to get the hacker's name
    ON t2.hacker_id = t3.hacker_id
ORDER BY
    submission_date;  -- order results by date

