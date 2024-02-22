SELECT s.id, s.student_fullname, AVG(g.grade)
FROM Students s 
JOIN Grades g ON s.id = g.student_id 
GROUP BY s.id,s.student_fullname 
ORDER BY g.grade  DESC
LIMIT(5)
