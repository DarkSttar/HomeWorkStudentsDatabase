WITH SSPTABLE AS(
SELECT g.student_id StudentID , s.student_fullname StudentName ,s2.id SubjectID , s2.subject_name SubjectName ,p.id ProfessorID , p.professor_name ProfessorName 
FROM Grades g 
JOIN Students s ON s.id = ? AND s.id = g.student_id
JOIN Subjects s2 ON s2.id = g.subject_id 
JOIN Professors p ON p.id = s2.professor_id AND p.id = ?
GROUP BY(s2.subject_name)
)
SELECT AVG(g.grade) Average ,ssp.StudentID,ssp.StudentName, ssp.ProfessorID,ssp.ProfessorName
FROM Grades g 
JOIN SSPTABLE ssp
WHERE g.student_id = ssp.StudentID AND g.subject_id = ssp.SubjectID