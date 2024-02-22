SELECT p.id , p.professor_name , s.subject_name 
FROM Subjects s 
JOIN Professors p ON p.id = ? AND s.professor_id = p.id 