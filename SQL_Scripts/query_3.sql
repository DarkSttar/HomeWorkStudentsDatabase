WITH GroupAverage AS (
SELECT g.id GroupID, g.group_name GroupName , AVG(gr.grade) Average , COUNT(gr.grade) CountGrades,sub.subject_name  
FROM Students s 
JOIN Groups g 
JOIN Grades gr ON s.id = gr.student_id AND s.group_id = g.id  AND gr.subject_id = ?
JOIN Subjects sub ON sub.id = gr.subject_id  
GROUP BY (g.group_name)
ORDER  BY(g.id)
)
SELECT ga.GroupID,ga.GroupName,COUNT(s.id) AS CountStudents,ga.Average, ga.CountGrades, ga.subject_name
FROM Students s
JOIN GroupAverage ga ON s.group_id = ga.GroupID
GROUP BY(ga.GroupID)