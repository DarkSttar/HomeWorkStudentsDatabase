WITH StudentAverage AS (
SELECT g.group_name, s.id,s.student_fullname,AVG(g1.grade) as Average
FROM Students s
JOIN Grades g1 ON g1.student_id = s.id
JOIN Groups g  ON s.group_id  = g.id
GROUP BY g.group_name ,s.id
ORDER BY s.id
)
SELECT g.id, sa.group_name,AVG(sa.Average) AS GroupAverage
FROM StudentAverage sa
JOIN Groups g ON g.group_name = sa.group_name
GROUP BY sa.group_name