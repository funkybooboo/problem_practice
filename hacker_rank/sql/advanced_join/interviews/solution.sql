SELECT
  c.contest_id,
  c.hacker_id,
  c.name,
  COALESCE(s.total_submissions,            0) AS total_submissions,
  COALESCE(s.total_accepted_submissions,   0) AS total_accepted_submissions,
  COALESCE(v.total_views,                  0) AS total_views,
  COALESCE(v.total_unique_views,           0) AS total_unique_views
FROM Contests AS c

-- aggregate submission stats by contest
LEFT JOIN (
  SELECT
    col.contest_id,
    SUM(ss.total_submissions)           AS total_submissions,
    SUM(ss.total_accepted_submissions) AS total_accepted_submissions
  FROM Colleges AS col
  JOIN Challenges AS ch
    ON col.college_id = ch.college_id
  LEFT JOIN Submission_Stats AS ss
    ON ch.challenge_id = ss.challenge_id
  GROUP BY col.contest_id
) AS s
  ON c.contest_id = s.contest_id

-- aggregate view stats by contest
LEFT JOIN (
  SELECT
    col.contest_id,
    SUM(vs.total_views)           AS total_views,
    SUM(vs.total_unique_views)    AS total_unique_views
  FROM Colleges AS col
  JOIN Challenges AS ch
    ON col.college_id = ch.college_id
  LEFT JOIN View_Stats AS vs
    ON ch.challenge_id = vs.challenge_id
  GROUP BY col.contest_id
) AS v
  ON c.contest_id = v.contest_id

WHERE
     COALESCE(s.total_submissions,          0) > 0
  OR COALESCE(s.total_accepted_submissions, 0) > 0
  OR COALESCE(v.total_views,                0) > 0
  OR COALESCE(v.total_unique_views,         0) > 0

ORDER BY
  c.contest_id;

