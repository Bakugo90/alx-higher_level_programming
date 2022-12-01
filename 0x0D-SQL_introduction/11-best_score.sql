-- list all records of data with score >= 10 in `second-table`
SELECT score, name
FROM `second_table`
WHERE `score` >= 10
ORDER BY score DISC
