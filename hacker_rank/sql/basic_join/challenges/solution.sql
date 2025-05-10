WITH challenge_counts AS (
    SELECT 
        h.hacker_id, 
        h.name, 
        COUNT(c.challenge_id) AS challenge_count
    FROM hackers h
    JOIN challenges c ON h.hacker_id = c.hacker_id
    GROUP BY h.hacker_id, h.name
),
count_frequencies AS (
    SELECT 
        challenge_count, 
        COUNT(*) AS freq
    FROM challenge_counts
    GROUP BY challenge_count
),
max_count AS (
    SELECT MAX(challenge_count) AS max_challenges FROM challenge_counts
)
SELECT 
    cc.hacker_id, 
    cc.name, 
    cc.challenge_count
FROM challenge_counts cc
JOIN count_frequencies cf 
    ON cc.challenge_count = cf.challenge_count
JOIN max_count mc
    ON 1=1
WHERE 
    cf.freq = 1 OR cc.challenge_count = mc.max_challenges
ORDER BY 
    cc.challenge_count DESC, 
    cc.hacker_id;

