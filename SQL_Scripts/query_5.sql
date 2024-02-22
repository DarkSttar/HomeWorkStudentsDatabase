SELECT s.subject_name,s.professor_id, p.professor_name
FROM Subjects s 
JOIN Professors p ON p.id = s.professor_id 