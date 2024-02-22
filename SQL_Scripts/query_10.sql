SELECT g.student_id , s.student_fullname , s2.subject_name,p.id , p.professor_name  
FROM Grades g 
JOIN Students s ON s.id = ? AND s.id = g.student_id
JOIN Subjects s2 ON s2.id = g.subject_id 
JOIN Professors p ON p.id = s2.professor_id AND p.id = ?
GROUP BY(s2.subject_name)