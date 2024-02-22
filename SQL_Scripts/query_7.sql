SELECT g.id, g.group_name, s.id, s.student_fullname, g2.grade, s2.subject_name  
FROM Students s 
JOIN Groups g ON s.group_id  = g.id AND g.id = ?
JOIN Grades g2 ON g2.student_id = s.id
JOIN Subjects s2 ON s2.id = ? AND g2.subject_id = s2.id  