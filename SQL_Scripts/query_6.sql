SELECT g.id, g.group_name, s.id, s.student_fullname
FROM Students s 
JOIN Groups g ON s.group_id  = g.id AND g.id = ?
