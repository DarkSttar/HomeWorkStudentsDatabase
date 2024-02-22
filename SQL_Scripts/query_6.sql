SELECT s.id,s.student_fullname, g.group_name 
FROM Students s 
JOIN Groups g ON s.group_id = g.id 
ORDER BY g.group_name 