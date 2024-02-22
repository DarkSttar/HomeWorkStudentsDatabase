WITH StudentAverage AS (
SELECT s.id, s.student_fullname,sb.subject_name, AVG(g.grade) as Average
FROM Students s
JOIN Grades g ON s.id = g.student_id 
JOIN Subjects sb ON g.subject_id = sb.id 
GROUP BY s.id, sb.id
ORDER BY Average DESC
)
SELECT s.id AS StudentID  ,s.student_fullname,sb.id AS SubjectID, s.subject_name,MAX(s.Average)
FROM StudentAverage s
JOIN Subjects sb ON sb.subject_name = s.subject_name
WHERE sb.id = ?
GROUP BY s.subject_name
