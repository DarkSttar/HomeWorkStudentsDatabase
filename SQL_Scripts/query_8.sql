SELECT p.id , p.professor_name , s.subject_name , AVG(g.grade) Average 
FROM Subjects s 
JOIN Professors p ON p.id = ? AND s.professor_id = p.id 
JOIN Grades g ON g.subject_id = s.id 
GROUP BY(s.id)