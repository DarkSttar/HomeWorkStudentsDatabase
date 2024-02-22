WITH StudentsAverage AS (
SELECT s.id, s.student_fullname, AVG(g.grade) AS Average
FROM Students s 
JOIN Grades g ON s.id = g.student_id 
GROUP BY s.id,s.student_fullname 
)
SELECT AVG(sa.Average)
FROM StudentsAverage AS sa