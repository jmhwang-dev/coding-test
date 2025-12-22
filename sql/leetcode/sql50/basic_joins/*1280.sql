-- ans1
SELECT 
    a.student_id, 
    a.student_name, 
    a.subject_name, 
    COUNT(e.student_id) AS attended_exams
FROM (
    SELECT *
    FROM Students
    CROSS JOIN Subjects
    ORDER BY student_id, subject_name
) a
LEFT JOIN Examinations e
    ON a.subject_name = e.subject_name 
    AND a.student_id = e.student_id
GROUP BY 
    a.student_id, 
    a.student_name, 
    a.subject_name;


-- ans2
WITH attended AS (
    SELECT 
        student_id, 
        subject_name, 
        COUNT(*) AS attended_exams
    FROM 
        Examinations
    GROUP BY 
        student_id, 
        subject_name
)
SELECT 
    s.student_id, 
    s.student_name, 
    sub.subject_name, 
    COALESCE(a.attended_exams, 0) AS attended_exams
FROM 
    Students s
CROSS JOIN 
    Subjects sub
LEFT JOIN 
    attended a 
    ON s.student_id = a.student_id 
    AND sub.subject_name = a.subject_name
ORDER BY 
    s.student_id, 
    sub.subject_name;

-- ans3
WITH attended AS (
    SELECT 
        student_id, 
        subject_name, 
        COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
),
default_info AS (
    SELECT *
    FROM Students
    CROSS JOIN Subjects
)
SELECT 
    di.student_id, 
    di.student_name, 
    di.subject_name, 
    COALESCE(a.attended_exams, 0) AS attended_exams
FROM default_info di
LEFT JOIN attended a
    USING (student_id, subject_name)
ORDER BY di.student_id, di.subject_name;

-- ans4
with CommonExam as (
    select *
    from Students st
    cross join Subjects su
),
CountAttend as (
    select student_id, subject_name, count(*) as attended_exams
    from Examinations
    group by student_id, subject_name
)

select ce.student_id, ce.student_name, ce.subject_name, coalesce(ca.attended_exams, 0) as attended_exams
from CommonExam ce
left join CountAttend ca
on ce.student_id = ca.student_id and ce.subject_name = ca.subject_name
order by ce.student_id, ce.student_name, ce.subject_name

-- best
SELECT 
    s.student_id, 
    s.student_name, 
    sub.subject_name, 
    COUNT(e.subject_name) AS attended_exams
FROM 
    Students s
CROSS JOIN 
    Subjects sub
LEFT JOIN 
    Examinations e 
    ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY 
    s.student_id, s.student_name, sub.subject_name
ORDER BY 
    s.student_id, sub.subject_name;